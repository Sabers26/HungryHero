from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import forms
from . import models
import uuid

# Create your views here.
def inicio(request):
    return render(request, 'myapp/index.html')

def registrar_cliente(request):
    data = {
        'mensaje': ""
    }
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['correo']
        username = request.POST['usuario']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        usr = User()
        usr.username = username
        usr.set_password(password)
        usr.save()
        
        cliente = models.Cliente()
        id_cli = uuid.uuid4()
        cliente.id_cliente = id_cli
        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.email = email
        cliente.cuenta = usr
        cliente.save()
        
        usuario = authenticate(username=username, password=password)
        login(request, usuario)
        return redirect(to=inicio)
    return render(request, 'registro/register.html', data)

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['password']
        
        usuario = authenticate(username=username, password=password)
        
        if usuario is not None:
            login(request, usuario)
            return redirect(to=inicio)
        else:
            data = {
                'mensaje': 'usuario o contraseña invalido. Intentelo nuevamente'
            }
    return render(request, 'registro/login.html')

def lista_platos(request):
    platos = models.Plato.objects.all()
    
    data = {
        'plato': platos
    }
    
    return render(request, 'platos/lista_platos.html', data)