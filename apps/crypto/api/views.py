from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.crypto.api.filters import CryptoCurrencyFilter, LastTradeFilter
from apps.crypto.models import CryptoCurrency, LastTrade
from apps.crypto.serializers import CryptoCurrencySerializer, LastTradeSerializer


class CryptoCurrencyViewSet(ReadOnlyModelViewSet):
    serializer_class = CryptoCurrencySerializer
    queryset = CryptoCurrency.objects.all()
    filter_class = CryptoCurrencyFilter


class LastTradeViewSet(ReadOnlyModelViewSet):
    serializer_class = LastTradeSerializer
    queryset = LastTrade.objects.all().order_by('-date')
    filter_class = LastTradeFilter
