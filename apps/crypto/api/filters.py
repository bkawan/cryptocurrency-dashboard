from django_filters import DateTimeFromToRangeFilter
from django_filters.rest_framework import FilterSet

from apps.crypto.models import CryptoCurrency, LastTrade


class CryptoCurrencyFilter(FilterSet):
    created_at = DateTimeFromToRangeFilter(name='created_at')

    class Meta:
        model = CryptoCurrency
        fields = ['bot', 'created_at', ]


class LastTradeFilter(FilterSet):
    class Meta:
        model = LastTrade
        fields = ['bot']
