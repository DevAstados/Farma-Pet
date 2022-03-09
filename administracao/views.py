from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from produto.models import Produto


class listagem_produto(ListView):
    template_name = 'listagem_produtos.html'

    def get_queryset(self):
        self.produtos = get_object_or_404(Produto)

        return self.produtos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def administracao(request):
    if request.method == 'GET':
        template_name = 'base_administracao.html'

        return render(request=request, template_name=template_name)


def login(request):
    pass


def Logout(request):
    if request.method == 'GET':
        auth.logout(request)

        return redirect('..')
