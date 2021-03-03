from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps.user.models import Usuarios


class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('prueba')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(** kwargs)
        context['title'] = 'Iniciar Sesión'
        return context


def lista(request):
    data = {
        'name': 'Hola',
        'usuarios': Usuarios.objects.all()
    }
    return render(request, 'usuarios/prueba.html', data)
