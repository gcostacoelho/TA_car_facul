"""project4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_principal'),
    path('cadastro_cliente/', cadastro_cliente),
    path('cadastro_veiculo/', cadastro_veiculo),
    path('lista_clientes/', lista_cliente, name="url_lista_clientes"),
    path('lista_veiculos/', lista_veiculo, name="url_lista_veiculos"),
    path('cadastro_fabricante', cadastro_fabricante),
    path('lista_fabricante', lista_fabricante),
    path('tabela/', tabela_preco),
    path('altera_cliente/<int:id>/', altera_cliente, name="url_altera_cliente"),
    path('altera_veiculo/<int:id>/', altera_veiculo, name="url_altera_veiculo"),
    path('exclui_cliente/<int:id>/', exclui_cliente, name="url_exclui_cliente"),
    path('exclui_veiculo/<int:id>/', exclui_veiculo, name="url_exclui_veiculo"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

