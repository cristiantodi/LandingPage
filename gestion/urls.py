from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
# from .views import crear_informacion_modelo

urlpatterns = [
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)