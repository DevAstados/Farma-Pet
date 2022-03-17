from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView

from produto.models import Produto


class listagem_produto(ListView):
    template_name = 'listagem_produtos.html'

    def get_queryset(self):
        self.produtos = Produto.objects.all()

        return self.produtos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


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
