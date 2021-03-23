from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from apps.cobranza.creditos.models import Creditos


class CreditDetail(LoginRequiredMixin, TemplateView):
    template_name = 'credit.html'
    model = Creditos

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle credito'
        context['entity'] = 'Credito'
        return context


@login_required
def credit_detail(request, credit_slug):
    credit = Creditos.objects.raw('select * from creditos '
                                  'inner join info_cliente on creditos.cliente = info_cliente.cliente and creditos.empresa = info_cliente.empresa WHERE clave = %s', [credit_slug])[:1]
    context = {
        'credit': credit[0],
        'title': 'Detalle credito',
        'entity': 'Credito',
    }
    return render(request, 'credit.html', context)
