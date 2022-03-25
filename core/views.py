from django.shortcuts import redirect, render
from core.forms import *
from core.models import *
# Create your views here.

def home(request):
    return render(request, './index.html')

def cadastro_cliente(request):
    form = FormCliente(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    
    contexto = {'form': form}
    return render(request, 'core/cadastro_cliente.html', contexto)

def lista_cliente(request):
    dados = Cliente.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_cliente.html', contexto)

def cadastro_veiculo(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form}
    return render(request, 'core/cadastro_veiculo.html', contexto)

def lista_veiculo(request):
    dados = Veiculo.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_veiculo.html', contexto)

def cadastro_fabricante(request):
    form = FormFabricante(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form}
    return render(request, 'core/cadastro_fabricante.html', contexto)


def tabela_preco(request):
    return render(request, 'core/tabela_preco.html')