from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^calendario2', views.crear_calendario2, name='calendario2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
