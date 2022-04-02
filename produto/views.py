from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from produto import models
from produto.models import Produto, Especificacoes, Categoria, Marca
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy


class home(ListView):
    template_name = 'produto/listagem_produto.html'

    def get_queryset(self):
        self.produtos = Produto.objects.all()
        return self.produtos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'categoria' in self.kwargs :
            context['categoria'] = get_object_or_404(Categoria, nome=self.kwargs['categoria'])
            context['produtos'] = Produto.getListProdutInColun(categoria=context['categoria'])
        else:
            context['produtos'] = Produto.getListProdutInColun()

        context['categorias'] = Categoria.objects.all().order_by('nome')[0:4]
        return context


class DetalheProduto(DetailView):
    model = models.Produto
    context_object_name = 'detalhe'
    template_name = 'produto/detalhe.html'

    def get_object(self):
        self.produto = get_object_or_404(Produto, slug=self.kwargs['slug'])
        return self.produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all().order_by('nome')[0:5]

        return context
