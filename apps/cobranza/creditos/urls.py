from django.urls import path

from apps.cobranza.creditos.views import credit_detail

app_name = 'creditos'

urlpatterns = [
    path('credito/<slug:empresa>/<slug:credito>/', credit_detail, name='credit_detail')
]
