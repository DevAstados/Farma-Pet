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

from utils.enviar_email import sending_pedido


class checkout(View):
    def post(self, request, *args, **kwargs):
        context = {}
        context['categorias'] = Categoria.objects.all().order_by('nome')[0:4]
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
        context['categorias'] = Categoria.objects.all().order_by('nome')[0:4]
        context['items'] = itens
        context['pedido'] = pedido
        context['endereco'] = endereco
        self.get_status(pedido=pedido, transaction_cod='78867D84A85242839AE62C9D049DBCF4')
        context['status_pagamento'] = pedido.status
        return render(request, template_name, context)

    def get_status(self, pedido, transaction_cod):
        pagseguro = PagSeguroApi()
        transaction = pagseguro.get_transaction(transaction_cod)
        time.sleep(2)
        transaction = transaction['transaction']

        if not pedido.transaction_code:
            pedido.transaction_code = transaction_cod

        if transaction['status'] == '1':
            pedido.status = 'Aguardando pagamento'
        elif transaction['status'] == '2':
            pedido.status = 'Em análise'
        elif transaction['status'] == '3':
            pedido.status = 'Paga'
        elif transaction['status'] == '4':
            pedido.status = 'Disponível'
        elif transaction['status'] == '5':
            pedido.status = 'Em disputa'
        elif transaction['status'] == '6':
            pedido.status = 'Devolvida'
        elif transaction['status'] == '7':
            pedido.status = 'Cancelada'
        pedido.save()

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
        pedido.save()
        Pedido.baixaEstoque(itens)
        for item in itens:
            ItemPedido.save(item)
        url = reverse('pedido:resumo', kwargs={'id': pedido.id})
        sending_pedido(pedido,itens)
        print(data['redirect_url'])
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver.execute_script("window.open('" + data['redirect_url'] + "', '_blank')")
        #driver.switch_to.window(driver.window_handles[1])

        return HttpResponseRedirect(url)
