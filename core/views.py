from django.shortcuts import redirect, render
from core.forms import *
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
    return render(request, 'core/lista_cliente.html')

def cadastro_veiculo(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    return render(request, 'core/cadastro_veiculo.html')

def lista_veiculo(request):
    return render(request, 'core/lista_veiculo.html')

def tabela_preco(request):
    return render(request, 'core/tabela_preco.html')