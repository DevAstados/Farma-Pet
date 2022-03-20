from django.views.generic.edit import CreateView, UpdateView, DeleteView
from produto.models import Produto, Especificacoes, Categoria, Marca
from django.views.generic import ListView
from django.urls import reverse_lazy


class administracao(ListView):
   pass

class ProdutoCreate(CreateView):
   model = Produto
   fields = ['nome', 'descricao', 'quantidade',  'imagem',  'preco', 'preco_promocional', 'categoria', 'especificacoes','marca']
   template_name = 'produto/form.html'
   success_url = reverse_lazy('listagem_produto')


class ProdutoUpdate(UpdateView):
   model = Produto
   fields = ['nome', 'descricao', 'quantidade',  'imagem',  'preco', 'preco_promocional', 'categoria', 'especificacoes','marca']
   template_name = 'produto/form.html'
   success_url = reverse_lazy('listagem_produto')

class ProdutoDelete(DeleteView):
   model = Produto
   template_name = 'produto/form.html'
   success_url = reverse_lazy('listagem_produto')

class EspecificacoesCreate(CreateView):
   model = Especificacoes
   fields = ['indicacao', 'raca', 'porte',  'idade',  'composicao', 'cor', 'fragrancia', 'peso','frequencia_recomendada','dimensoes']
   template_name = 'produto/form.html'
   success_url = reverse_lazy('listagem_produto')


class EspecificacoesUpdate(UpdateView):
   model = Especificacoes
   fields = ['indicacao', 'raca', 'porte',  'idade',  'composicao', 'cor', 'fragrancia', 'peso','frequencia_recomendada','dimensoes']
   template_name = 'produto/form.html'
   success_url = reverse_lazy('listagem_produto')

class EspecificacoesDelete(DeleteView):
   model = Especificacoes
   template_name ='produto/form.html'
   success_url = reverse_lazy('listagem_produto')


class CategoriaCreate(CreateView):
   model = Categoria
   fields = ['Nome']
   template_name = 'produto/form.html'
   success_url = reverse_lazy('listagem_produto')


class CategoriaUpdate(UpdateView):
   model = Categoria
   fields = ['Nome']
   template_name = 'produto/form.html'
   success_url = reverse_lazy('listagem_produto')

class CategoriaDelete(DeleteView):
   model = Categoria
   template_name = 'produto/form.html'
   success_url = reverse_lazy('listagem_produto')

class MarcaCreate(CreateView):
   model = Marca
   fields = ['Nome']
   template_name = 'produto/form.html'
   success_url = reverse_lazy('listagem_produto')


class MarcaUpdate(UpdateView):
   model = Marca
   fields = ['Nome']
   template_name = 'produto/form.html'
   success_url = reverse_lazy('listagem_produto')

class MarcaDelete(DeleteView):
   model = Marca
   template_name = 'produto/form.html'
   success_url = reverse_lazy('listagem_produto')