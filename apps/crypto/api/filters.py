from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import FilterSet

from apps.crypto.models import CryptoCurrency


class CryptoCurrencyFilter(FilterSet):
    created_at = DateFromToRangeFilter(name='created_at')

    class Meta:
        model = CryptoCurrency
        fields = ['bot',
                  'created_at',
                  ]




