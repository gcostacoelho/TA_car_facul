from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from core.models import *


class FormFabricante(ModelForm):
    class Meta:
        model = Fabricante
        fields = '__all__'

class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class FormVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

class FormFabricante(ModelForm):
    class Meta:
        model = Fabricante
        fields = '__all__'

class FormRotativo(ModelForm):
    class Meta:
        model = Rotativo
        fields = '__all__'


class FormCadastroRotativo(ModelForm):
    class Meta:
        model = Rotativo
        fields = ['data_entrada', 'id_veiculo', 'id_preco']


class FormMensalista(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'

