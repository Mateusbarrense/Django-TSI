# Importamos a função index() definida no arquivo views.py
from django.urls import path
from . import views
from website.views import FuncionarioCreateView, ListaFuncionarios, IndexTemplateView, FuncionarioUpdateView, FuncionarioDeleteView


app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET /
    path('funcionarios', views.index, name='index'),

    path('', views.IndexTemplateView.as_view(), name='index'),

    path('funcionarios_lista/', ListaFuncionarios.as_view(), name='lista_funcionarios'),

    path('funcionario/<int:pk>', FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),
    
    # path('funcionario/<slug:slug>', FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),

    path('funcionario/excluir/<int:pk>', FuncionarioDeleteView.as_view(), name='deleta_funcionario'),    

    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(), name='cadastra_funcionario'),    
]