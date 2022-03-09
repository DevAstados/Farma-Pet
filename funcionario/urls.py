import debug_toolbar
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
