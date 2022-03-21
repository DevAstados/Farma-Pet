import json

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView

from funcionario.models import Funcionario
from produto.forms import FormProduto
from produto.models import Produto, Categoria, Marca, Especificacoes


class listagem_produto(ListView):
    template_name = 'listagem_produtos.html'

    def get_queryset(self):
        self.produtos = Produto.objects.all()

        return self.produtos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class listagem_funcionario(ListView):
    template_name = 'listagem_funcionario.html'

    def get_queryset(self):
        self.funcionario = Funcionario.objects.all()

        return self.funcionario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class listagem_cliente(ListView):
    template_name = 'listagem_cliente.html'

    def get_queryset(self):
        self.produtos = Produto.objects.all()

        return self.produtos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class listagem_pedido(ListView):
    template_name = 'listagem_pedido.html'

    def get_queryset(self):
        self.produtos = Produto.objects.all()

        return self.produtos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class adicionar_produto(CreateView):
   model = Produto
   fields = ['nome', 'descricao', 'quantidade',  'imagem',  'preco', 'preco_promocional', 'categoria', 'especificacoes','marca']
   template_name = 'adicionar_produto.html'
   success_url = reverse_lazy('listagem_produto')


class adicionar_produto(CreateView):
    template_name = 'adicionar_produto.html'

    def get(self, request, *args, **kwargs):
        template_name = 'adicionar_produto.html'
        context = {}
        context['categorias'] = Categoria.objects.all()
        context['marcas'] = Marca.objects.all()
        return render(request, template_name,context=context)

    def post(self, request, *args, **kwargs):

        requestJson = json.dumps(request.POST,separators=(',', ':'))
        requestJson = json.loads(requestJson)

        if(requestJson['categoria-nome'] != ''):
            categoria = Categoria.popular(requestJson['categoria-nome'])
            Categoria.save(categoria)
        else:
            categoria = get_object_or_404(Categoria,pk=requestJson['categoria-select'])
        if(requestJson['marca-nome'] != ''):
            marca = Marca.popular(requestJson['marca-nome'])
            Marca.save(marca)
        else:
            marca = get_object_or_404(Marca,pk=requestJson['marca-select'])

        especificacoes = Especificacoes.popular(requestJson)
        Especificacoes.save(especificacoes)

        produto = Produto.popular(requestJson,categoria,marca,especificacoes).save()




        return redirect('listagem_produto')



class alterar_produto(View):
    template_name = 'listagem_produtos.html'

    def get_queryset(self):
        self.produto = get_object_or_404(Produto, pk=self.kwargs['id'])
        return self.produto


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def administracao(request):
    if request.method == 'GET':
        template_name = 'base_administracao.html'

        return render(request=request, template_name=template_name)


def excluirProduto(request, id):
    if request.method == 'GET':
        get_object_or_404(Produto, pk=id).delete()
        return redirect('listagem_produto')


def login(request):
    pass


def Logout(request):
    if request.method == 'GET':
        auth.logout(request)

        return redirect('..')
