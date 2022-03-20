from django.urls import path
from produto.views import *

urlpatterns = [
    path('cadastrar/produto/', ProdutoCreate.as_view(), name='cadastrar-produto'),
    path('editar/produto/<int:pk>/', ProdutoUpdate.as_view(), name='editar-produto'),
    path('excluir/produto/<int:pk>/', ProdutoDelete.as_view(), name='excluir-produto'),
    path('cadastrar/especificacoes/', EspecificacoesCreate.as_view(), name='cadastrar-especificacoes'),
    path('editar/especificacoes/<int:pk>/', EspecificacoesUpdate.as_view(), name='editar-especificacoes'),
    path('excluir/especificacoes/<int:pk>/', EspecificacoesDelete.as_view(), name='excluir-especificacoes'),
    path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar-categoria'),
    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir-categoria'),
    path('cadastrar/marca/', MarcaCreate.as_view(), name='cadastrar-marca'),
    path('editar/marca/<int:pk>/', MarcaUpdate.as_view(), name='editar-marca'),
    path('excluir/marca/<int:pk>/', MarcaDelete.as_view(), name='excluir-marca'),

]
