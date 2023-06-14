from django.shortcuts import render, redirect
from . import models
import uuid

# Create your views here.
def inicio(request):
    return render(request, 'myapp/index.html')

def nuevo_ing(request):
    data = {
                'mensaje': ""
    }
    if request.method == 'POST':
        nombreIng = request.POST.get('nombreIngrediente')
        unidad = request.POST.get('unidadMedida')
        id_ing = uuid.uuid4()
        
        try:
            ing = models.Ingrediente(id_ing, nombreIng, unidad)
            
            ing.save()
            
            data = {
                'mensaje': "Ingrediente guardado correctamente"
            }
        except Exception as e:
            data = {
                'mensaje': "No se pudo guardar el Ingrediente"
            }
    return render(request, 'myapp/ingredientes/nuevo_ingrediente.html', data)


def listado_ing(request):
    ing = models.Ingrediente.objects.all()
    
    data = {
        'ingrediente': ing
    }
    return render(request, 'myapp/ingredientes/listar_ingredientes.html', data)