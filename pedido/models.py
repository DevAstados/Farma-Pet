from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from pagseguro.api import PagSeguroItem, PagSeguroApi

from cliente.models import Cliente, Endereco
from funcionario.models import Funcionario
from produto.models import Produto


class FormaDePagamento(models.Model):
    forma_de_pagamento = models.CharField(unique=True, max_length=30)

    def _str_(self):
        return self.forma_de_pagamento

    class Meta:
        verbose_name = 'Forma de Pagamento'
        verbose_name_plural = 'Formas de Pagamentos'


class Transportadora(models.Model):
    nome_transportadora = models.CharField(unique=True, max_length=50)
    telefone = models.CharField(max_length=11)

    def _str_(self):
        return self.nome_transportadora

    class Meta:
        verbose_name = 'Transportadora'
        verbose_name_plural = 'Transportadoras'


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    total = models.FloatField()
    forma_pagamento = models.CharField(max_length=20, blank=True)
    data = models.DateTimeField()
    subtotal = models.FloatField()
    transaction_code = models.CharField(max_length=100,blank=True, null=True)
    desconto = models.FloatField(default=0.0)
    codigo_rastreio = models.CharField(unique=True, max_length=50, blank=True, null=True)
    notal_fiscal = models.CharField(max_length=70, blank=True, null=True)
    endereco_entrega = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=50,default="Aguardando")
    def _str_(self):
        return f' N. {self.pk}.zfill(6)'

    @classmethod
    def criarPedido(cls, cliente, endereco, formaDePagamento='Pagseguro'):
        pedido = Pedido()
        pedido.data = datetime.today()
        pedido.cliente = cliente
        pedido.forma_pagamento = formaDePagamento
        pedido.endereco_entrega = endereco

        return pedido

    @classmethod
    def calcularCaixa(cls, items):
        subtotal = 0
        desconto = 0

        for item in items:
            subtotal += item.preco * item.quantidade
            desconto += (item.preco - item.preco_promocional) * item.quantidade
        total = subtotal - desconto

        return subtotal, total, desconto

    @classmethod
    def baixaEstoque(cls, items):

        for item in items:
            produto = Produto.objects.get(id=item.produto.id)
            produto.quantidade -= item.quantidade
            Produto.save(produto)

    @classmethod
    def getPedidoByUser(cls, user):
        listPedido = []

        for pedido in Pedido.objects.all().filter(vendedor=user):
            listPedido.append(pedido)

        return listPedido

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=250)
    largura = models.IntegerField(blank=True, null=True)
    altura = models.IntegerField(blank=True, null=True)
    comprimento = models.IntegerField(blank=True, null=True)

    def _str_(self):
        return f'Item do {self.pedido}'

    @classmethod
    def criarItemPedido(cls, pedido, produto,imagem,
                        preco_promocional=0, quantidade=1):
        item = ItemPedido()
        item.pedido = pedido
        item.produto = produto
        item.preco = produto.preco
        item.preco_promocional = produto.preco_promocional
        item.quantidade = quantidade
        item.imagem = imagem

        return item

    @classmethod
    def criarListItensPedido(cls, pedido, reqJson):
        itens = []
        for item in reqJson:
            produto = Produto.objects.get(id=item['id'])
            itens.append(
                ItemPedido.criarItemPedido(pedido=pedido, produto=produto,
                                           imagem=item['imagem'],
                                           quantidade=item['quantity']))

        return itens

    @classmethod
    def criarListItensPedidoPag(cls, produtos):
        pagseguro_api = PagSeguroApi()
        pagseguro_api
        for item in produtos:
            produto = Produto.objects.get(id=item['id'])
            if produto.preco_promocional:
                pagseguro_api.add_item(
                    PagSeguroItem(id=f'{produto.id}'.zfill(4), description=produto.nome, amount=produto.preco_promocional,
                                  quantity=item['quantity']))
        return pagseguro_api



    @classmethod
    def getItensPedido(cls, pedido_id):
        pedido_itens = ItemPedido.objects.filter(pedido_id=pedido_id)
        itens = []
        for item in pedido_itens:
            itens.append(item)

        return itens

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'
