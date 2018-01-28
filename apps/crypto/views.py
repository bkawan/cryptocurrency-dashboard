# Create your views here.

from django.db.models import Sum
from django.utils.html import mark_safe
from django.views.generic import TemplateView

from apps.crypto.models import CryptoCurrency


class DashboardView(TemplateView):
    template_name = 'crypto/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        _sums = CryptoCurrency.objects.values('bot', 'currency').annotate(Sum('balance')).order_by('bot')
        sums = {}
        for x in _sums:
            sums.setdefault(x['bot'].lower(), {}).update({x['currency'].lower():x['balance__sum']})

        ctx['sums'] = mark_safe(sums)
        return ctx
