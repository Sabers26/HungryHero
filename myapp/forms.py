from django.forms import ModelForm
from . import models

class IngredienteForm(ModelForm):
    
    class Meta:
        model = models.Ingrediente
        fields = ['nombre_ing', 'unidad_medida']