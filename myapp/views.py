from django.shortcuts import render
from . import forms
from . import models
import uuid

# Create your views here.
def inicio(request):
    return render(request, 'myapp/index.html')

def nuevo_ing(request):
    if request.method == 'POST':
        nombreIng = request.POST.get('nomre_ing')
        unidad = request.POST.get('unidad_medida')
        
        id_ing = str(uuid.uuid4)
        
        ing = models.Ingrediente(id_ing, nombreIng, unidad)
        
        ing.save()
        
    data = {
        'formularioING': forms.IngredienteForm()
    }
    return render(request, 'myapp/ingredientes/nuevo_ingrediente.html', data)