from django_filters import DateFilter
from django_filters.rest_framework import FilterSet

from apps.crypto.models import CryptoCurrency


class CryptoCurrencyFilter(FilterSet):
    end_date = DateFilter(name="created_at", lookup_expr='gte')
    start_date = DateFilter(name="created_at", lookup_expr='gte')

    class Meta:
        model = CryptoCurrency
        fields = ['currency', 'bot', 'profit', 'balance', 'start_date', 'end_date']
