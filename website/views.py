from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView
from OlaMundo.models import Funcionario
from django import forms

from website.forms import AtualizaFuncionarioForm, InsereFuncionarioForm

class ListaFuncionarios(ListView):
    template_name = "website/funcionarios_lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


def index(request):
    return lista_funcionarios(request)


# Create your views here.
def lista_funcionarios(request):
    print(request)
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objects.all()

    # Contexto é o conjunto de dados que estarão disponíveis na página web que será retornada ao usuário.
    contexto = {'funcionarios': funcionarios}

    # Retornamos o template para listar os funcionários
    return render(request, "website/funcionarios.html", contexto)


class FuncionarioUpdateView(UpdateView):
    template_name = 'website/atualiza.html'
    model = Funcionario
    form_class = AtualizaFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")
    # fields = [
    #     # 'nome',
    #     # 'sobrenome',
    #     # 'cpf',
    #     # 'tempo_de_servico',
    #     'remuneracao'
    # ]
     

class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy(
    "website:lista_funcionarios"
)


class FuncionarioCreateView(CreateView):
    template_name = "website/inclui.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")