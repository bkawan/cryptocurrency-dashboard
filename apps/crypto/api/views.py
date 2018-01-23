from dateutil.parser import parse
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.crypto.api.filters import CryptoCurrencyFilter
from apps.crypto.models import CryptoCurrency
from apps.crypto.serializers import CryptoCurrencySerializer


class CryptoCurrencyViewSet(ReadOnlyModelViewSet):
    serializer_class = CryptoCurrencySerializer
    queryset = CryptoCurrency.objects.all()

    filter_class = CryptoCurrencyFilter

    # def get_queryset(self):
        # qs = super().get_queryset()
        # bot = self.request.query_params.get('bot')
        # if bot:
        #     qs = qs.filter(bot=bot)
        # start_date = self.request.query_params.get('start_date')
        # end_date = self.request.query_params.get('end_date')
        # if end_date and start_date:
        #     start_date = parse(start_date).date()
        #     end_date = parse(end_date).date()
        #     qs = qs.filter(created_at__range=(start_date, end_date))
        # return qs
