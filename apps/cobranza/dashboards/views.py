from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.cobranza.creditos.models import Gestores


@login_required
def dashboard_manager(request):
    credits = Gestores.objects.get(idusuario = 'aandrade')

    context = {
        'credits': credits,
        'title': 'Dashboard ' + request.user.username,
        'entity': 'Credito',
    }
    return render(request, 'dashboardManager.html', context)