# Create your views here.
from django.utils.html import mark_safe
from django.views.generic import TemplateView

from apps.crypto.models import LastTrade


class DashboardView(TemplateView):
    template_name = 'crypto/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['last_trades'] = mark_safe(list(LastTrade.objects.all().order_by('-id')
                                            .values('id', 'info', 'value', 'quantity', 'volume'))[:10])
        return ctx
