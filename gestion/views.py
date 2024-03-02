from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages

from users.models import User
from .forms import CustomAuthenticationForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.warning(self.request, 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.')
        return super().form_invalid(form)

    def form_valid(self, form):
        # Llama al método form_valid() de la clase padre para realizar la autenticación
        super().form_valid(form)
        # Redirige al usuario a la página de datos del usuario
        
        return redirect('datos_usuario')

@login_required
def datos_usuario(request):
    user_info = {
        'username': request.user.username,
        'email': request.user.email,
        'fullName': request.user.fullName,
        # Agrega más campos según tus necesidades
    }
    # Aquí obtienes y muestras los datos del usuario según tus necesidades
    return render(request, 'datos_usuario.html')

@login_required
def cerrar_sesion(request):
    logout(request)
    # messages.success(request, '¡Has cerrado sesión exitosamente!')
    # return redirect('login')
    return redirect(settings.LOGIN_URL) 

