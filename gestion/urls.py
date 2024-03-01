from django.urls import path
from .views import CustomLoginView, datos_usuario

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('datos-usuario/', datos_usuario, name='datos_usuario'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)