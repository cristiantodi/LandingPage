from django import forms
from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import redirect

from .models import InformacionModelo

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.IntegerField()
    password = str(forms.IntegerField(widget=forms.PasswordInput)) 

# -------------------------------------------------------------------------------

class gestionForm(forms.ModelForm):
	class Meta:
		model = InformacionModelo
		fields = ['observacion', 'comentario']