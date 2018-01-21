# Create your views here.
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'crypto/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
