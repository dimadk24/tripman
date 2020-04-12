from django.contrib import admin
from django.contrib.admin import register, AdminSite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

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
    pass


@register(Client, site=tripman_admin_site)
class ClientAdmin(admin.ModelAdmin):
    pass


@register(Trip, site=tripman_admin_site)
class TripAdmin(admin.ModelAdmin):
    readonly_fields = ('price',)
    edit_fields = ('client', 'trip_definition', 'sell_date', 'price')
    add_fields = ('client', 'trip_definition', 'sell_date')

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
    pass
