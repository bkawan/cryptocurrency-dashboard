# Create your views here.
from django.db.models.functions import *
from django.utils.html import mark_safe
from django.views.generic import TemplateView

from apps.crypto.models import LastTrade


class DashboardView(TemplateView):
    template_name = 'crypto/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['last_trades'] = mark_safe(list(LastTrade.objects.all().order_by('-id')
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
        return ctx
