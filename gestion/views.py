from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

from django.shortcuts import render, redirect

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'

def datos_usuario(request):
    # Aquí obtienes y muestras los datos del usuario según tus necesidades
    return render(request, 'datos_usuario.html')