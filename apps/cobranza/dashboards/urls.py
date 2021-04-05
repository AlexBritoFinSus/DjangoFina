from django.urls import path

from apps.cobranza.dashboards.views import dashboard_manager

app_name = 'dashboard'

urlpatterns = [
    path('manager', dashboard_manager, name='dashboardManager')
]
