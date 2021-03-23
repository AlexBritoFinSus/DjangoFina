from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.cobranza.creditos.models import Creditos


@login_required
def dashboard_manager(request):
    credits = Creditos.objects.raw('select creditos.* from creditos inner join gestores on creditos.credito = gestores.credito and creditos.empresa = gestores.empresa WHERE gestores.idusuario = %s', ['aandrade'])

    context = {
        'credits': credits,
        'title': 'Dashboard ' + request.user.username,
        'entity': 'Credito',
    }
    return render(request, 'dashboardManager.html', context)