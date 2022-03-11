from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, './index.html')

def cadastro_cliente(request):
    return render(request, 'core/cadastro_cliente.html')

def lista_cliente(request):
    return render(request, 'core/lista_cliente.html')

def cadastro_veiculo(request):
    return render(request, 'core/cadastro_veiculo.html')

def lista_veiculo(request):
    return render(request, 'core/lista_veiculo.html')

def tabela_preco(request):
    return render(request, 'core/tabela_preco.html')