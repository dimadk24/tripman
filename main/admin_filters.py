from datetime import timedelta

from django.contrib import admin
from django.db.models import Q
from django.utils import timezone


class HotTripDefinitionListFilter(admin.SimpleListFilter):
    title = 'Горящие путевки'
    parameter_name = 'hot'

    def lookups(self, request, model_admin):
        return (
            ('hot', 'Только горящие'),
            ('cold', 'Только не горящие'),
        )

    def queryset(self, request, queryset):
        now = timezone.now()
        five_days_in_future = now + timedelta(5)
        print(now)
        print(five_days_in_future)
        if self.value() == 'hot':
            return queryset.filter(start_date__lte=five_days_in_future,
                                   start_date__gte=now)
        if self.value() == 'cold':
            return queryset.filter(Q(start_date__gt=five_days_in_future) |
                                   Q(start_date__lt=now))
