from django.contrib import admin
from django.contrib.admin import register, AdminSite
from django.contrib.auth.models import Group, User

from .models import Trip, TripDefinition, Client, Service


class TripManAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = 'TripMan'
    # Text to put in each page's <h1> (and above login form).
    site_header = 'TripMan'
    # Text to put at the top of the admin index page.
    index_title = 'TripMan - сервис управления турагенством'


tripman_admin_site = TripManAdminSite()

tripman_admin_site.register(User)
tripman_admin_site.register(Group)


@register(TripDefinition, site=tripman_admin_site)
class TripDefinitionAdmin(admin.ModelAdmin):
    pass


@register(Client, site=tripman_admin_site)
class ClientAdmin(admin.ModelAdmin):
    pass


@register(Trip, site=tripman_admin_site)
class TripAdmin(admin.ModelAdmin):
    pass


@register(Service, site=tripman_admin_site)
class ServiceAdmin(admin.ModelAdmin):
    pass
