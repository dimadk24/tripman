from django.contrib import admin
from django.contrib.admin import register, AdminSite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
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


tripman_admin_site = TripManAdminSite()

tripman_admin_site.register(User, UserAdmin)


@register(TripDefinition, site=tripman_admin_site)
class TripDefinitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'location', 'start_date', 'end_date',
                    'calculated_number_of_trips')
    list_filter = ('location', 'start_date', 'end_date',
                   HotTripDefinitionListFilter)
    actions = None

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
    list_display = ('name', 'discount')
    list_filter = ('discount', 'trip__trip_definition__location')
    actions = None


@register(Trip, site=tripman_admin_site)
class TripAdmin(admin.ModelAdmin):
    list_display = ('client', 'trip_definition', 'price', 'sell_date')
    readonly_fields = ('price',)
    edit_fields = ('client', 'trip_definition', 'sell_date', 'price')
    add_fields = ('client', 'trip_definition', 'sell_date')
    list_filter = ('client', 'trip_definition', 'price', 'sell_date')
    actions = None

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
    actions = None
