from django.db import models
from django.contrib.auth.models import User

import re

'''
from pycep_correios import get_address_from_cep, WebService, exceptions
'''

from utils import validacpf

class Cliente(models.Model):
    email = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11)

    @classmethod
    def validacao(cls, cliente):
        error = []
        if not validacpf.valida_cpf(cliente.cpf):
            error.append('CPF Inválido')
        if cliente.nome == '' or cliente.nome == None:
            error.append('Por favor digite o nome do cliente')
        if cliente.sobrenome == '' or cliente.sobrenome == None:
            error.append('Por favor digite o sobrenome do cliente')

        r = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
        if not r.match(cliente.email):
            error.append('Por favor digite um email valido')
        r = re.compile(r'^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$')
        # if not r.match(cls.telefone):
        # error.append('Por favor digte um telefone valido (xx) xxxxx-xxxx ')
        return error

    @classmethod
    def splitNome(cls, nome):
        nome = re.findall(r'\S+', nome)
        cls.nome = nome[0]

        if len(nome) > 1:

            cls.sobrenome = nome[1]
            for i in range(2, len(nome)):
                cls.sobrenome += f' {nome[i]}'
            return cls.nome, cls.sobrenome
        return cls.nome, ""

    @classmethod
    def popular_cliente(cls, form):
        cliente = Cliente()
        cliente.nome, cliente.sobrenome = Cliente.splitNome(form['nome'])
        cliente.telefone = re.sub('[^0-9]', '',  form['numero_telefone'])
        cliente.email = form['email']
        cliente.cpf = re.sub('[^0-9]', '', form['cpf'])

        return cliente

    def _str_(self):
        return self.nome

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

'''
class Endereco(models.Model):
    tipo = models.CharField(max_length=30)
    numero = models.CharField(max_length=6)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    @classmethod
    def getEndereco(cls, pedido):
        endereco = get_address_from_cep(pedido.endereco_entrega.cep, webservice=WebService.VIACEP)
        endereco['numero'] = pedido.endereco_entrega.numero
        return endereco

    def _str_(self):
        return f' Tipo: {self.tipo}, do cliente {self.cliente.nome}{self.cliente.sobrenome}'

    @classmethod
    def populaEndereco(cls, form, cliente):
        endereco = Endereco()

        endereco.tipo = form['tipo_endereco']
        endereco.numero = form['numero_casa']
        endereco.complemento = form['complemento']
        endereco.cep = form['cep']
        endereco.cliente = cliente

        return endereco

    @classmethod
    def validacao(cls, endereco):
        error = []

        if not endereco.numero.isdigit():
            error.append('Por favor digitar somente digitos no campo número')

        try:
            get_address_from_cep(endereco.cep, webservice=WebService.VIACEP)
        except exceptions.InvalidCEP as eic:
            error.append('CEP Inválido')

        except exceptions.CEPNotFound as ecnf:
            error.append('CEP não encontrado')
        return error

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços' 
'''