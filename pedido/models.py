from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
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
    forma_pagamento = models.ForeignKey(FormaDePagamento, models.DO_NOTHING)
    data = models.DateTimeField()
    subtotal = models.FloatField()
    desconto = models.FloatField(default=0.0)
    frete = models.FloatField(null=True)
    codigo_rastreio = models.CharField(unique=True, max_length=50, blank=True, null=True)
    notal_fiscal = models.CharField(max_length=70, blank=True, null=True)
    vendedor = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)
    endereco_entrega = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING)

    def _str_(self):
        return f' N. {self.pk}.zfill(6)'

    @classmethod
    def criarPedido(cls, cliente, formaDePagamento, vendedor, endereco):
        pedido = Pedido()
        pedido.data = datetime.today()
        pedido.frete = 0.0
        pedido.cliente = cliente
        pedido.forma_pagamento = formaDePagamento
        pedido.vendedor = vendedor
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
    cor = models.CharField(max_length=50, blank=True, null=True)
    material = models.CharField(max_length=50, blank=True, null=True)
    largura = models.IntegerField(blank=True, null=True)
    altura = models.IntegerField(blank=True, null=True)
    comprimento = models.IntegerField(blank=True, null=True)

    def _str_(self):
        return f'Item do {self.pedido}'

    @classmethod
    def criarItemPedido(cls, pedido, produto, cor, material, largura, altura, comprimento, imagem,
                        preco_promocional=0, quantidade=1):
        item = ItemPedido()
        item.pedido = pedido
        item.produto = produto
        item.preco = produto.preco_marketing
        item.preco_promocional = produto.preco_marketing_promocional
        item.quantidade = quantidade
        item.imagem = imagem
        item.cor = cor
        item.material = material
        item.largura = largura if largura == None else 0
        item.altura = altura if altura == None else 0
        item.comprimento = comprimento if comprimento == None else 0
        return item

    @classmethod
    def criarListItensPedido(cls, pedido, reqJson):
        itens = []
        for item in reqJson:
            produto = Produto.objects.get(id=item['id'])
            itens.append(
                ItemPedido.criarItemPedido(pedido=pedido, produto=produto, cor=item['cor'], material=item['material'],
                                           largura=item['largura'], altura=item['altura'],
                                           comprimento=item['comprimento'], imagem=item['imagem'],
                                           quantidade=item['quantity']))

        return itens

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