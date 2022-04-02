from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from administracao import views

app_name = 'usuario'


urlpatterns = [
                  path('createUserGoogle/', views.CreateUserGoogle.as_view(), name='createUserGoogle'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)