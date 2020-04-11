from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'TripMan'

class TripManAdminConfig(AdminConfig):
    default_site = 'main.admin.TripManAdminSite'
