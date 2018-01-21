from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.crypto.api.filters import CryptoCurrencyFilter
from apps.crypto.models import CryptoCurrency
from apps.crypto.serializers import CryptoCurrencySerializer


class CryptoCurrencyViewSet(ReadOnlyModelViewSet):
    serializer_class = CryptoCurrencySerializer
    queryset = CryptoCurrency.objects.all()
    filter_class = CryptoCurrencyFilter
