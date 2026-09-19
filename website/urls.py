# Importamos a função index() definida no arquivo views.py
from django.urls import path
from . import views

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET /
    # path('', views.index, name='index'),
    path('', views.IndexTemplateView.as_view(), name='index'),

    path('funcionarios_lista/', views.ListaFuncionarios.as_view(), name='lista_funcionarios'),

    path(
        'funcionario/<int:pk>',
        views.FuncionarioUpdateView.as_view(),
        name='atualiza_funcionario'),

    path(
        'funcionario/excluir/<int:pk>',
        views.FuncionarioDeleteView.as_view(),
        name='deleta_funcionario'),    

    path(
        'funcionario/cadastrar/',
        views.FuncionarioCreateView.as_view(),
        name='cadastra_funcionario'),    
]