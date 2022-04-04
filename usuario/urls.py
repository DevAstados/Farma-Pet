from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from usuario import views

app_name = 'usuario'


urlpatterns = [
                  path('login_cliente/', views.login_cliente.as_view(), name='login_cliente'),
                  path('cadastro_cliente/', views.cadastro_cliente.as_view(), name='cadastro_cliente'),
                  path('cadastro_endereco/', views.cadastro_endereco.as_view(), name='cadastro_endereco'),
                  path('verificacao/', views.verificacao.as_view(), name='verificacao_cadastro'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)