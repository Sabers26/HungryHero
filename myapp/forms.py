from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class NuevoPlatoForm(forms.ModelForm):
    
    class Meta:
        model = models.Plato
        fields = ['nombre_plato', 'precio_plato', 'stock_plato', 'estado_plato', 'descripcion', 'imagen']