from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from usuario import views

app_name = 'usuario'


urlpatterns = [
                  path('login_cliente/', views.login_cliente.as_view(), name='login_cliente'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)