from distutils.command.upload import upload
from email.policy import default
from optparse import BadOptionError
from tabnanny import verbose
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=50, blank=True, null=True)
    foto =models.ImageField(upload_to='fotos_clientes', blank=True, null=True)
    
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Clientes'

class Fabricante(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name_plural = 'Fabricantes'


class Veiculo(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField(default=2022, blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    placa = models.CharField(max_length=10)
    foto =models.ImageField(upload_to='fotos_veiculos', blank=True, null=True)

    def __str__(self):
        return f'{self.placa} ({self.modelo})'
    class Meta:
        verbose_name_plural = 'Veiculos'
