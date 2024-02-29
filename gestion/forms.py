from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.IntegerField()
    password = str(forms.IntegerField(widget=forms.PasswordInput)) 
