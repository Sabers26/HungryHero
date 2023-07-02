from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from .models import *
import uuid

id_usuario = any

# Create your views here.
def inicio(request):
    platos = Plato.objects.all()
    
    data = {
        'platos': platos
    }
    return render(request, 'myapp/index.html', data)

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

@permission_required('myapp.add_plato')
def lista_platos(request):
    platos = Plato.objects.all()
    
    data = {
        'plato': platos
    }
    
    return render(request, 'platos/lista_platos.html', data)

@permission_required('myapp.add_plato')
def nuevo_plato(request):
    
    data = {
        'mensaje': ''
    }
    
    if request.method == 'POST':
        form = NuevoPlatoForm(request.POST)
        
        if form.is_valid():
            form.save()
            data['mensaje'] = 'Plato Guardado con exito'
        else:
            data['mensaje'] = 'No se pudo guardar el plato'
    '''if request.method == 'POST':
        nombre = request.POST['nombrePlato']
        precio = request.POST['precioPlato']
        stock = request.POST['stockPlato']
        estado = request.POST['estado']
        desc = request.POST['descripcion']
        foto = request.FILES['imagen']
        
        p = models.Plato()
        id_plato = uuid.uuid4()
        
        p.id_plato = id_plato
        p.nombre_plato = nombre
        p.precio_plato = precio
        p.stock_plato = stock
        p.descripcion = desc
        p.estado_plato = estado
        p.imagen = foto
        p.save()
        
        data = {
            'mensaje': 'Plato Guardado correctamente'
        }'''

    return render(request, 'platos/nuevo_plato.html', data)

@permission_required('myapp.add_plato')
def eliminar_plato(request, id):
    plato = Plato.objects.get(id_plato = id)
    data = {
        'plato': plato.nombre_plato
    }
    if request.method == 'POST':
        plato.delete()
        return redirect(to=lista_platos)
    
    return render(request, 'platos/eliminar_plato.html', data)

@permission_required('myapp.add_plato')
def modificar_plato(request, id):
    p = Plato.objects.get(id_plato=id)
    data = {
        'plato': p,
        'desc': str(p.descripcion)
    }
    
    if request.method == 'POST':
        nombre = request.POST['nombrePlato']
        precio = request.POST['precioPlato']
        stock = request.POST['stockPlato']
        estado = request.POST['estado']
        desc = request.POST['descripcion']
        
        p.nombre_plato = nombre
        p.precio_plato = precio
        p.stock_plato = stock
        p.descripcion = desc
        p.estado_plato = estado
        p.save()
        
        data = {
            'mensaje': 'Plato Modificado correctamente'
        }
        return redirect(to=lista_platos)
    return render(request, 'platos/modificar_plato.html', data)

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect(to=inicio)