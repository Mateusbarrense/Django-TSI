# Importamos a função index() definida no arquivo views.py
from django.urls import path
from . import views

# from Website.views import FuncionarioListView

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET /
    path('', views.index, name='index'),

    path('funcionarios_lista/', views.ListaFuncionarios.as_view(), name='lista_funcionarios'),
]