from django.contrib import admin
from django.contrib.admin import register, AdminSite
from django.db.models import Count

from .admin_filters import HotTripDefinitionListFilter
from .models import Trip, TripDefinition, Client, Service


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


@register(TripDefinition, site=tripman_admin_site)
class TripDefinitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'location', 'start_date', 'end_date',
                    'calculated_number_of_trips')
    list_filter = ('location', 'start_date', 'end_date',
                   HotTripDefinitionListFilter)

    def calculated_number_of_trips(self, obj):
        return obj.number_of_trips

    calculated_number_of_trips.admin_order_field = 'number_of_trips'
    calculated_number_of_trips.short_description = 'Путешествий'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(number_of_trips=Count('trip'))
        return queryset


@register(Client, site=tripman_admin_site)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'discount_in_money')
    list_filter = ('discount', 'trip__trip_definition__location')
    actions = ('get_sum_discount',)

    def discount_in_money(self, obj):
        discount = 0
        trips = obj.trip_set.all()
        for trip in trips:
            discount += trip.trip_definition.price - trip.price
        return discount

    discount_in_money.short_description = 'Суммарная скидка (руб)'

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
    list_filter = ('client', 'trip_definition', 'price', 'sell_date')

    def save_model(self, request, obj: Trip, form, change):
        obj.price = obj.price or obj.trip_definition.price * (
            100 - obj.client.discount) / 100
        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj: Trip = None):
        if obj:
            return self.edit_fields
        return self.add_fields


@register(Service, site=tripman_admin_site)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
