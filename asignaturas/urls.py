from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^calendario', views.crear_calendario, name='calendario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
