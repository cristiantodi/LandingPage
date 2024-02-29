from django.urls import path
from .views import CustomLoginView

from .views import datos_usuario

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),

    path('datos-usuario/', datos_usuario, name='datos_usuario'),
]