from rest_framework.serializers import ModelSerializer

from apps.crypto.models import CryptoCurrency, LastTrade


class CryptoCurrencySerializer(ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = "__all__"


class LastTradeSerializer(ModelSerializer):
    class Meta:
        model = LastTrade
        fields = "__all__"
