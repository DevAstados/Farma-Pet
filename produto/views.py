from django.views.generic.edit import CreateView, UpdateView, DeleteView
from produto.models import Produto, Especificacoes, Categoria, Marca
from django.views.generic import ListView
from django.urls import reverse_lazy


class home(ListView):
    template_name = 'produto/listagem_produto.html'

    def get_queryset(self):
        self.produtos = Produto.objects.all()
        return self.produtos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['produtos'] = Produto.getListProdutInColun()
        context['categorias'] = Categoria.objects.all().order_by('nome')[0:4]
        return context
