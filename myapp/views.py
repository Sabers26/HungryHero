from django.shortcuts import render
from . import forms
from . import models
import uuid

# Create your views here.
def inicio(request):
    return render(request, 'myapp/index.html')

def nuevo_ing(request):
    if request.method == 'POST':
        nombreIng = request.POST.get('nombreIngrediente')
        unidad = request.POST.get('unidadMedida')
        id_ing = uuid.uuid4()
        
        ing = models.Ingrediente(id_ing, nombreIng, unidad)
        
        ing.save()
        
    return render(request, 'myapp/ingredientes/nuevo_ingrediente.html')