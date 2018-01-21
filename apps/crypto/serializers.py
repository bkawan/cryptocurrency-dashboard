from rest_framework.serializers import ModelSerializer

from apps.crypto.models import CryptoCurrency


class CryptoCurrencySerializer(ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = "__all__"
