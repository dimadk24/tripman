from admin_actions.admin import ActionsModelAdmin
from django.contrib import admin
from django.contrib.admin import register, AdminSite
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django.db.models import Count
from django.shortcuts import redirect
from django.urls import reverse
from rangefilter.filter import DateRangeFilter

from .admin_filters import HotTripDefinitionListFilter
from .models import Trip, TripDefinition, Client, Service, Excursion, City, \
    Hotel


class TripManAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = 'TripMan'
    # Text to put in each page's <h1> (and above login form).
    site_header = 'TripMan'
    # Text to put at the top of the admin index page.
    index_title = 'TripMan - сервис управления турагенством'

    index_template = 'admin/tripman_index.html'


tripman_admin_site = TripManAdminSite()
tripman_admin_site.disable_action('delete_selected')

tripman_admin_site.register(User, UserAdmin)
tripman_admin_site.register(Group, GroupAdmin)


@register(TripDefinition, site=tripman_admin_site)
class TripDefinitionAdmin(ActionsModelAdmin):
    list_display = ('name', 'price', 'start_date', 'end_date',
                    'calculated_number_of_trips')
    list_filter = (('start_date', DateRangeFilter),
                   ('end_date', DateRangeFilter),
                   HotTripDefinitionListFilter)
    readonly_fields = ('created_by',)
    actions_list = ('open_random_trip_definition',)

    def open_random_trip_definition(self, request):
        trip_def = TripDefinition.objects.raw('CALL RandomTripDefinition();')[0]
        return redirect(reverse('admin:main_tripdefinition_change',
                                args=[trip_def.pk]))

    open_random_trip_definition.short_description = 'Случайная путевка'
    open_random_trip_definition.url_path = 'random'

    def calculated_number_of_trips(self, obj):
        return obj.number_of_trips

    calculated_number_of_trips.admin_order_field = 'number_of_trips'
    calculated_number_of_trips.short_description = 'Путешествий'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(number_of_trips=Count('trip'))
        return queryset

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


@register(Client, site=tripman_admin_site)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'total_saved')
    list_filter = ('discount',)
    actions = ('get_sum_discount',)

    def get_sum_discount(self, request, queryset):
        sum_discount = 0
        for item in queryset:
            sum_discount += self.discount_in_money(item)
        self.message_user(request, f'Суммарная скидка: {sum_discount} руб')

    get_sum_discount.short_description = 'Посчитать суммарную скидку'


@register(Trip, site=tripman_admin_site)
class TripAdmin(admin.ModelAdmin):
    list_display = ('client', 'trip_definition', 'price', 'sell_date')
    readonly_fields = ('price',)
    edit_fields = ('client', 'trip_definition', 'sell_date', 'price')
    add_fields = ('client', 'trip_definition', 'sell_date')
    list_filter = ('client', 'trip_definition', 'price',
                   ('sell_date', DateRangeFilter))

    def get_fields(self, request, obj: Trip = None):
        if obj:
            return self.edit_fields
        return self.add_fields


@register(Service, site=tripman_admin_site)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)


@register(Excursion, site=tripman_admin_site)
class ExcursionAdmin(admin.ModelAdmin):
    list_display = ('name', 'times_included', 'times_visited',)
    readonly_fields = ('times_included', 'times_visited',)


@register(City, site=tripman_admin_site)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@register(Hotel, site=tripman_admin_site)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city',)
