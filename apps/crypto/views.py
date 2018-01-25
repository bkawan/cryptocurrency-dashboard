# Create your views here.
from collections import defaultdict

from django.db.models import Sum
from django.db.models.functions import *
from django.utils.html import mark_safe
from django.views.generic import TemplateView

from apps.crypto.models import LastTrade, CryptoCurrency


class DashboardView(TemplateView):
    template_name = 'crypto/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['last_trades'] = mark_safe(list(LastTrade.objects.all().order_by('-date')
                                            .annotate(year=ExtractYear('date'),
                                                      month=ExtractMonth('date'),
                                                      day=ExtractDay('date'),
                                                      hour=ExtractHour('date'),
                                                      minute=ExtractMinute('date'),
                                                      second=ExtractSecond('date'),
                                                      )
                                            .values('id',
                                                    'info',
                                                    'value',
                                                    'quantity',
                                                    'volume',
                                                    'year',
                                                    'month',
                                                    'day',
                                                    'hour',
                                                    'minute',
                                                    'second',

                                                    ))[:10])

        _sums = CryptoCurrency.objects.values('bot', 'currency').annotate(Sum('balance')).order_by('bot')
        sums = {}

        for x in _sums:
            sums.setdefault(x['bot'].lower(), {}).update({x['currency'].lower():x['balance__sum']})

        ctx['sums'] = mark_safe(sums)
        return ctx
