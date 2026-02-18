from django.urls import path
from django.urls import include 
from core.views import *

urlpatterns = [
       path('', login_usuario, name='login_usuario'),
       path('dashboard/', DashboardView.as_view(), name='dashboard'),
       path("importar-xlsx/", ImportarXlsxReceitasView.as_view(), name="importar_xlsx_receitas"),
       path("importar-xlsx-despesas/",ImportarXlsxDespesasView.as_view(), name="importar_xlsx_despesas"),
       path("bootstrap-admin/", bootstrap_admin, name="super_admin"),
   ]