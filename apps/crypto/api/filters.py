from datetime import timedelta
from django.utils.datetime_safe import datetime
from django_filters import DateFromToRangeFilter, ChoiceFilter, DateTimeFromToRangeFilter
from django_filters.rest_framework import FilterSet

from apps.crypto.models import CryptoCurrency


class CryptoCurrencyFilter(FilterSet):
    # HOURLY_CHOICES = (
    #     ('last', 'Last Hour'),
    # )
    created_at = DateTimeFromToRangeFilter(name='created_at')
    # hourly = ChoiceFilter(choices=HOURLY_CHOICES,name='created_at', method='get_hourly')

    class Meta:
        model = CryptoCurrency
        fields = ['bot',
                  'created_at',
                  # 'hourly',
                  ]

    # def get_hourly(self, queryset, name, value):
    #     if value == 'last':
    #         return queryset.filter(created_at__range=((datetime.now()-timedelta(hours=1)),datetime.now()))
    #     return queryset
