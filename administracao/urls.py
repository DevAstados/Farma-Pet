from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from administracao import views

urlpatterns = [
                  path('login/', views.login, name='login'),
                  path('logout/', views.Logout, name='logout'),
                  path('', views.administracao, name='administracao'),
                  path('listagemProduto', views.listagem_produto.as_view(), name='listagem_produto'),
                  path('deletarProduto/<id>', views.excluirProduto, name='deletar_produto'),
                  path('alteraProduto/<id>', views.alterar_produto.as_view(), name='alterar_produto'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
