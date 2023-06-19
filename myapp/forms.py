from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CrearCuentaForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',]

class CrearClienteForm(forms.ModelForm):
    
    class Meta:
        model = models.Cliente
        fields = ['nombre', 'apellido', 'email']