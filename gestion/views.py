from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages

from .forms import CustomAuthenticationForm, gestionForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.warning(self.request, 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.')
        return super().form_invalid(form)

    def form_valid(self, form):
        super().form_valid(form)        
        return redirect('datos_usuario')

@login_required
def datos_usuario(request):
    user_info = {
        'username': request.user.username,
        'email': request.user.email,
        'fullName': request.user.fullName,
        }
    return render(request, 'datos_usuario.html')

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def gracias(request):
    logout(request)
    return redirect('gracias')



def contactPage(request):
    form = gestionForm()
    return render(request, "datos_usuario.html", {"contactForm": form})

##-----------------------------------------------------------------------------------------------------

def postContact(request):
    if request.method == 'POST':
        form = gestionForm(request.POST)
        if form.is_valid():
            form.save()
            if request.method == 'POST':
                logout(request) 
                print("----------------------------------------------------------------")
                return render(request,'gracias.html')
            return redirect('datos_usuario')  # Cambia esto a la vista que desees después de guardar
    else:
        form = gestionForm()

    return render(request, 'datos_usuario.html', {'form': form})