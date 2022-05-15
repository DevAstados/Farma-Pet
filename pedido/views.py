import json
import time

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from webdriver_manager.chrome import ChromeDriverManager

from cliente.models import Cliente, Endereco
from pedido.models import ItemPedido, Pedido
from produto.models import Categoria, Produto
from pagseguro.api import PagSeguroItem, PagSeguroApi
from selenium import webdriver


class checkout(View):
    def post(self, request, *args, **kwargs):
        context = {}
        context['categorias'] = Categoria.objects.all().order_by('nome')
        return render(request, 'checkout.html', context)


class resumo(View):
    global template_name

    def get(self, request, *args, **kwargs):
        template_name = 'createPedido.html'
        pedido_id = kwargs.get('id')

        pedido = Pedido.objects.get(id=pedido_id)
        itens = ItemPedido.getItensPedido(pedido_id=pedido.id)

        endereco = Endereco.getEndereco(pedido)
        context = {}
        context['categorias'] = Categoria.objects.all().order_by('nome')
        context['items'] = itens
        context['pedido'] = pedido
        context['endereco'] = endereco
        pagseguro = PagSeguroApi()
        context['status_pagamento'] = pagseguro.get_notification()
        return render(request, template_name, context)


class pagar(View):

    def post(self, request, *args, **kwargs):
        requestJson = json.loads(request.body.decode('utf-8'))
        cliente = Cliente.objects.get(usuario_id=request.user.id)
        endereco = Endereco.objects.get(cliente=cliente)
        pedido = Pedido.criarPedido(cliente=cliente,
                                    endereco=endereco)
        itens = ItemPedido.criarListItensPedido(pedido=pedido, reqJson=requestJson['cart'])
        pedido.subtotal, pedido.total, pedido.desconto = Pedido.calcularCaixa(itens)

        pagseguro_api = ItemPedido.criarListItensPedidoPag(produtos=requestJson['cart'])
        data = pagseguro_api.checkout()

        pedido.transaction_code = data['code']
        pedido.save()
        Pedido.baixaEstoque(itens)
        for item in itens:
            ItemPedido.save(item)
        url = reverse('pedido:resumo', kwargs={'id': pedido.id})

        print(data['redirect_url'])
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.execute_script("window.open('" + data['redirect_url'] + "', '_blank')")
        driver.switch_to.window(driver.window_handles[1])

        return HttpResponseRedirect(url)
