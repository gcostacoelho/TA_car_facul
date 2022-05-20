from django.shortcuts import redirect, render
from core.forms import *
from core.models import *
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request, './index.html')

class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/register.html'

#Cliente
def cadastro_cliente(request):
    form = FormCliente(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    
    contexto = {'form': form, 'titulo': 'Cadastro de cliente', 'stringBotao': 'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)
"""    render = É uma resposta sem código para quem solicitou acesso ao server"""
def lista_cliente(request):
    dados = Cliente.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_cliente.html', contexto)

def altera_cliente(request, id):
    objeto = Cliente.objects.get(id=id)
    form = FormCliente(request.POST or None, request.FILES or None, instance=objeto)
    
    if form.is_valid():
        form.save()
        contexto = {'objeto': objeto.nome, 'url': '/lista_clientes/', 'titulo': 'Atualização de clientes', 'stringBotao': 'Atualizar'}
        return render(request, 'core/mensagem_salva.html', contexto)
    
    contexto = {'form': form, 'titulo': 'Atualização de clientes', 'stringBotao': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)

def exclui_cliente(request, id):
    objeto = Cliente.objects.get(id=id)
    if request.POST:
        objeto.delete()
        return redirect('url_lista_clientes')
    contexto = {'url': '/lista_clientes', 'objeto': objeto.nome}
    return render(request, 'core/mensagem_excluir.html', contexto)

#Veiculos
def cadastro_veiculo(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form, 'titulo': 'Cadastro de veículos', 'stringBotao': 'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)

def lista_veiculo(request):
    dados = Veiculo.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_veiculo.html', contexto)

def altera_veiculo(request, id):
    objeto  = Veiculo.objects.get(id=id)
    form = FormVeiculo(request.POST or None, request.FILES or None, instance=objeto)

    if form.is_valid():
        form.save()
        contexto = {'objeto': objeto.modelo, 'url': '/lista_veiculos/', 'titulo': 'Atualização de veículos', 'stringBotao': 'Atualizar'}
        return render(request, 'core/mensagem_salva.html', contexto)
    
    contexto = {'form': form, 'titulo': 'Atualização de veículos', 'stringBotao': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)

def exclui_veiculo(request, id):
    objeto = Veiculo.objects.get(id=id)
    if request.POST:
        objeto.delete()
        return redirect('url_lista_veiculos')
    contexto = {'url': '/lista_veiculos', 'objeto': objeto.modelo}
    return render(request, 'core/mensagem_excluir.html', contexto)

#Fabricante
def cadastro_fabricante(request):
    form = FormFabricante(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form, 'titulo': 'Cadastro de fabricantes', 'stringBotao': 'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)

def lista_fabricante(request):
    dados = Fabricante.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_fabricante.html', contexto)

#Preços
def tabela_preco(request):
    dados = Preco.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/tabela_preco.html', contexto)

#Rotativo
def cadastro_rotativo(request):
    form = FormCadastroRotativo(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_lista_rotativo')
    contexto = {'form': form, 'titulo':'Cadastro de rotativo', 'stringBotao': 'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)

def listagem_rotativo(request):
    dados = Rotativo.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_rotativo.html', contexto)

def altera_rotativo(request, id):

    objeto = Rotativo.objects.get(id=id)
    form = FormRotativo(request.POST or None, request.FILES or None, instance=objeto)

    if form.is_valid():
        objeto.calcula_total()
        form.save()
        return redirect('url_lista_rotativo')
        
    contexto = {'form': form, 'titulo':'Atualização de rotativo', 'stringBotao': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)

#Mensalista
def cadastro_mensalista(request):
    form = FormMensalista(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_lista_mensalista')
    contexto = {'form': form, 'titulo':'Cadastro de mensalista', 'stringBotao': 'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)

def listagem_mensalista(request):
    dados = Mensalista.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_mensalista.html', contexto)

def altera_mensalista(request, id):
    objeto = Mensalista.objects.get(id=id)
    form = FormMensalista(request.POST or None, request.FILES or None, instance=objeto)

    if form.is_valid():
        form.save()
        context = {'objeto': objeto.id_cliente, 'url': '/lista_mensalista/', 'titulo': 'Atualização de mensalistas', 'stringBotao': 'Atualizar'}
        return render(request, 'core/mensagem_salva.html', context)
    
    contexto = {'form': form, 'titulo': 'Atualização de mensalistas', 'stringBotao': 'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)

def exclui_mensalista(request, id):
    objeto = Mensalista.objects.get(id=id)
    if request.POST:
        objeto.delete()
        return redirect('url_lista_mensalista')
    contexto = {'url': '/lista_mensalista', 'objeto': objeto.id_cliente}
    return render(request, 'core/mensagem_excluir.html', contexto)