from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView
from OlaMundo.models import Funcionario
from django import forms

class ListaFuncionarios(ListView):
    template_name = "website/funcionarios_lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

def index(request):
    return lista_funcionarios(request)

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"

# Create your views here.
def lista_funcionarios(request):

    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objects.all()

    # Incluímos no contexto
    # Contexto é o conjunto de dados que estarão disponíveis na página web que será retornada ao usuário.
    contexto = {'funcionarios': funcionarios}

    # Retornamos o template para listar os funcionários
    return render(request, "website/funcionarios.html", contexto)

class FuncionarioUpdateView(UpdateView):
    template_name = 'website/atualiza.html'
    model = Funcionario
    fields = [
        'nome',
        'sobrenome',
        'cpf',
        'tempo_de_servico',
        'remuneracao'
]

class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy(
    "website:lista_funcionarios"
)

class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        # Modelo base
        model = Funcionario
        # Campos que estarão no form
        fields = [
        'nome',
        'sobrenome',
        'cpf',
        'remuneracao'
        ]
        # Campos que não estarão no form
        exclude = [
        'tempo_de_servico'
        ]

class FuncionarioCreateView(CreateView):
    template_name = "website/inclui.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")