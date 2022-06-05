import json

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from funcionario.models import Funcionario
from produto.forms import FormProduto
from produto.models import Produto, Categoria, Marca, Especificacoes
from usuario.models import CustomUser


class login(View):

    def get(self, request, *args, **kwargs):
        template_name = 'login_funcionario.html'

        return render(request, template_name)

    def post(self, request, *args, **kwargs):
        requestJson = json.dumps(request.POST, separators=(',', ':'))
        requestJson = json.loads(requestJson)

        usuario = CustomUser(email=requestJson['username'])
        usuario.set_password(requestJson['password'])
        usuario = authenticate(email=usuario.email, password=requestJson['password'])
        if not usuario:
            messages.add_message(request, messages.ERROR, "Usuário ou senha incorreto")

            return redirect(request.path_info)
        elif usuario.tipo_usuario == 'C':
            messages.add_message(request, messages.ERROR, "Usuário não é um funcionario")
            return redirect(request.path_info)

        auth.login(request, user=usuario)
        return redirect(reverse_lazy('adm:administracao'))


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
    template_name = 'adicionar_produto.html'

    def get(self, request, *args, **kwargs):
        template_name = 'adicionar_produto.html'
        context = {}
        context['categorias'] = Categoria.objects.all()
        context['marcas'] = Marca.objects.all()
        return render(request, template_name, context=context)

    def post(self, request, *args, **kwargs):

        requestJson = json.dumps(request.POST, separators=(',', ':'))
        requestJson = json.loads(requestJson)

        if (requestJson['categoria-nome'] != ''):
            categoria = Categoria.popular(requestJson['categoria-nome'])
            Categoria.save(categoria)
        else:
            categoria = get_object_or_404(Categoria, pk=requestJson['categoria-select'])
        if (requestJson['marca-nome'] != ''):
            marca = Marca.popular(requestJson['marca-nome'])
            Marca.save(marca)
        else:
            marca = get_object_or_404(Marca, pk=requestJson['marca-select'])

        especificacoes = Especificacoes.popular(requestJson)
        Especificacoes.save(especificacoes)

        produto = Produto.popular(requestJson, categoria, marca, especificacoes).save()

        return redirect('adm:listagem_produto')


class adicionar_funcionario(CreateView):
    template_name = 'adicionar_funcionario.html'

    def get(self, request, *args, **kwargs):
        template_name = 'adicionar_funcionario.html'
        context = {}

        return render(request, template_name, context=context)

    def post(self, request, *args, **kwargs):
        requestJson = json.dumps(request.POST, separators=(',', ':'))
        requestJson = json.loads(requestJson)
        usuario = CustomUser.popular(requestJson, tipo_usuario='F')

        funcionario = Funcionario.popular(requestJson, usuario=usuario)
        usuario.save()
        Funcionario.save(funcionario)

        return redirect('adm:listagem_funcionario')


class update_produto(View):
    template_name = 'alterar_produto.html'

    def get(self, request, *args, **kwargs):
        template_name = 'alterar_produto.html'
        context = {}
        context['produto'] = get_object_or_404(Produto, pk=self.kwargs['id'])

        context['categorias'] = Categoria.objects.all()
        context['marcas'] = Marca.objects.all()
        return render(request, template_name, context=context)

    def post(self, request, *args, **kwargs):
        requestJson = json.dumps(request.POST, separators=(',', ':'))
        requestJson = json.loads(requestJson)

        produto = get_object_or_404(Produto, pk=self.kwargs['id'])
        especificacoes = get_object_or_404(Especificacoes, pk=produto.especificacoes.pk)

        especificacoes = Especificacoes.popular_alterar(requestJson, especificacoes)
        produto = Produto.popular_alterar(requestJson, produto)
        Especificacoes.save(especificacoes)
        Produto.save(produto)

        return redirect('listagem_produto')


class update_funcionario(View):

    def get(self, request, *args, **kwargs):
        template_name = 'alterar_funcionario.html'
        context = {}
        context['funcionario'] = get_object_or_404(Funcionario, pk=self.kwargs['id'])

        return render(request, template_name, context=context)

    def post(self, request, *args, **kwargs):
        requestJson = json.dumps(request.POST, separators=(',', ':'))
        requestJson = json.loads(requestJson)

        funcionario = get_object_or_404(Funcionario, pk=self.kwargs['id'])
        usuario = get_object_or_404(CustomUser, pk=funcionario.usuario.pk)

        funcionario = Funcionario.popularAlteracao(requestJson, funcionario)
        usuario = CustomUser.popularalteracao(requestJson,usuario)
        usuario.save()
        Funcionario.save(funcionario)

        return redirect('adm:listagem_funcionario')


def administracao(request):
    if request.method == 'GET':
        template_name = 'base_administracao.html'

        return render(request=request, template_name=template_name)


def excluirProduto(request, id):
    if request.method == 'GET':
        get_object_or_404(Produto, pk=id).delete()
        return redirect('adm:listagem_produto')


def excluirFuncionario(request, id):
    if request.method == 'GET':
        funcionario = get_object_or_404(Funcionario, pk=id)
        usuario = get_object_or_404(CustomUser, pk=funcionario.usuario.pk)

        funcionario.delete()
        usuario.delete()
        return redirect('adm:listagem_funcionario')


def cadastrado_google(request):
    print(request.user.password)


def Logout(request):
    if request.method == 'GET':
        auth.logout(request)

        return redirect('adm:login')
