from django.shortcuts import render
from django.views.generic import ListView
from OlaMundo.models import Funcionario


class ListaFuncionarios(ListView):
    template_name = "website/funcionarios_lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

def index(request):
    return lista_funcionarios(request)

# Create your views here.
def lista_funcionarios(request):

    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objects.all()

    # Incluímos no contexto
    # Contexto é o conjunto de dados que estarão disponíveis na página web que será retornada ao usuário.
    contexto = {'funcionarios': funcionarios}

    # Retornamos o template para listar os funcionários
    return render(request, "website/funcionarios.html", contexto)