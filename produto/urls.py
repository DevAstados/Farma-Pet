from django.urls import path

from produto import views
from produto.views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'produtos'

urlpatterns = [
                  path("<slug:slug>/", views.DetalheProduto.as_view(),
                       name='detalhe')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
