from django.shortcuts import redirect, render
from core.forms import *
from core.models import *
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'index.html')

class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/register.html'

#Cliente
def cadastro_cliente(request):
    try:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            form.save()
            messages.success(request, f'Cliente {nome} cadastrado com sucesso!')
            return redirect('url_lista_clientes')
        
        contexto = {'form': form, 'titulo': 'Cadastro de cliente', 'stringBotao': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)
    """    render = É uma resposta sem código para quem solicitou acesso ao server"""

def lista_cliente(request):
    try:
        dados = Cliente.objects.all()
        if request.POST:
            if request.POST['pesquisa']: dados = Cliente.objects.filter(nome=request.POST['pesquisa'])

        contexto = {'dados': dados}
        return render(request, 'core/lista_cliente.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

def altera_cliente(request, id):
    try:
        objeto = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=objeto)
        
        if form.is_valid():
            nome = form.cleaned_data['nome']
            form.save()
            messages.success(request, f'Cliente {nome} atualizado com sucesso')
            return redirect('url_lista_clientes')
        
        contexto = {'form': form, 'titulo': 'Atualização de clientes', 'stringBotao': 'Atualizar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

def exclui_cliente(request, id):
    try:
        objeto = Cliente.objects.get(id=id)
        if request.POST:
            objeto.delete()
            return redirect('url_lista_clientes')
        contexto = {'url': '/lista_clientes', 'objeto': objeto.nome}
        return render(request, 'core/mensagem_excluir.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

#Veiculos
def cadastro_veiculo(request):
    try:
        form = FormVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form': form, 'titulo': 'Cadastro de veículos', 'stringBotao': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

def lista_veiculo(request):
    try:
        dados = Veiculo.objects.all()
        if request.POST:
            if request.POST['pesquisa']: dados=Veiculo.objects.filter(placa=request.POST['pesquisa'])
        contexto = {'dados': dados}
        return render(request, 'core/lista_veiculo.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

def altera_veiculo(request, id):
    try:
        objeto  = Veiculo.objects.get(id=id)
        form = FormVeiculo(request.POST or None, request.FILES or None, instance=objeto)

        if form.is_valid():
            nome = form.cleaned_data['modelo']
            form.save()
            messages.success(request, f'{nome} atualzado com sucesso')
            return redirect('url_lista_veiculos')
        
        contexto = {'form': form, 'titulo': 'Atualização de veículos', 'stringBotao': 'Atualizar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

def exclui_veiculo(request, id):
    try:
        objeto = Veiculo.objects.get(id=id)
        if request.POST:
            objeto.delete()
            return redirect('url_lista_veiculos')
        contexto = {'url': '/lista_veiculos', 'objeto': objeto.modelo}
        return render(request, 'core/mensagem_excluir.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

#Fabricante
def cadastro_fabricante(request):
    try:
        form = FormFabricante(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form': form, 'titulo': 'Cadastro de fabricantes', 'stringBotao': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

def lista_fabricante(request):
    try:
        dados = Fabricante.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/lista_fabricante.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

#Preços
def tabela_preco(request):
    try:
        dados = Preco.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/tabela_preco.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

#Rotativo
def cadastro_rotativo(request):
    try:
        form = FormCadastroRotativo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_lista_rotativo')
        contexto = {'form': form, 'titulo':'Cadastro de rotativo', 'stringBotao': 'Cadastrar', 'calendario': True}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

def listagem_rotativo(request):
    try:
        dados = Rotativo.objects.all()
        if request.POST:
            if request.POST['pesquisa']: dados=Rotativo.objects.filter(id_veiculo=int(request.POST['pesquisa']))
        contexto = {'dados': dados}
        return render(request, 'core/lista_rotativo.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

def altera_rotativo(request, id):
    try:
        objeto = Rotativo.objects.get(id=id)
        form = FormRotativo(request.POST or None, request.FILES or None, instance=objeto)

        if form.is_valid():
            objeto.calcula_total()
            veiculo = form.cleaned_data['id_veiculo']
            form.save()
            messages.success(request, f'{veiculo} atualizado com sucesso')
            return redirect('url_lista_rotativo')
            
        contexto = {'form': form, 'titulo':'Atualização de rotativo', 'stringBotao': 'Atualizar', 'calendario': True}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

#Mensalista
def cadastro_mensalista(request):
    try:
        form = FormMensalista(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_lista_mensalista')
        contexto = {'form': form, 'titulo':'Cadastro de mensalista', 'stringBotao': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

def listagem_mensalista(request):
    try:
        dados = Mensalista.objects.all()
        if request.POST:
            if request.POST['pesquisa']: dados=Mensalista.objects.filter(id_cliente=int(request.POST['pesquisa']))
        contexto = {'dados': dados}
        return render(request, 'core/lista_mensalista.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

def altera_mensalista(request, id):
    try:
        objeto = Mensalista.objects.get(id=id)
        form = FormMensalista(request.POST or None, request.FILES or None, instance=objeto)

        if form.is_valid():
            nome = form.cleaned_data['id_cliente']
            form.save()
            messages.success(request, f'Mensalista {nome} atualizado com sucesso')
            return redirect('url_lista_mensalista')

        contexto = {'form': form, 'titulo': 'Atualização de mensalistas', 'stringBotao': 'Atualizar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)

def exclui_mensalista(request, id):
    try:
        objeto = Mensalista.objects.get(id=id)
        if request.POST:
            objeto.delete()
            return redirect('url_lista_mensalista')
        contexto = {'url': '/lista_mensalista', 'objeto': objeto.id_cliente}
        return render(request, 'core/mensagem_excluir.html', contexto)
    except Exception as mensagem_erro:
        contexto = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto)