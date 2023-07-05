from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from .models import *
import uuid
from django.shortcuts import get_object_or_404
from django.db.models import F

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
        
        cliente = Cliente()
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

@login_required
def carrito(request):
    usuario = User.objects.get(username=request.user.username)
    carrito = CarritoCompras.objects.get(usuario=usuario, estado=False)
    elemento_carrito = ElementoCarrito.objects.filter(carrito=carrito)
    
    data = {
        'elemento_carrito': elemento_carrito,
        'rango_cantidad': None
    }
    if request.method == 'POST':
        
        for elemento in elemento_carrito:
            cantidad = request.POST.get('cantidad_{}'.format(elemento.plato.id_plato))
            elemento.cantidad = int(cantidad)
            elemento.calcular_subTotal()
            elemento.save()
            plato = Plato.objects.get(id_plato=elemento.plato.id_plato)
            cantidad_int = int(cantidad)
            plato.stock_plato -= cantidad_int
            plato.save()
        
        carrito.estado = True
        carrito.actualizar_total()
        carrito.save()
        return redirect(to='inicio')
    
    rango_cantidad = range(1, max(elemento.plato.stock_plato for elemento in elemento_carrito) + 1)
    data['rango_cantidad'] = rango_cantidad
    return render(request, 'carrito/carrito.html', data)

@login_required
def agregar_carrito(request, id_plato):
    id_plato = uuid.UUID(id_plato)
    plato = get_object_or_404(Plato, id_plato=id_plato)
    
    usuario = User.objects.get(username=request.user.username)
    carrito, created = CarritoCompras.objects.get_or_create(usuario=usuario)
    
    if not created:
        carrito = CarritoCompras.objects.get(usuario=usuario)
    
    elemento_carrito = ElementoCarrito.objects.filter(carrito=carrito, plato=plato)
    
    if not elemento_carrito.exists():
        elemento_carrito = ElementoCarrito()
        elemento_carrito.carrito = carrito
        elemento_carrito.plato = plato
        elemento_carrito.cantidad = 1
        elemento_carrito.calcular_subTotal()
        elemento_carrito.save()
    
    return redirect('carrito')

def eliminar_carrito(request, id_plato):
    usuario = User.objects.get(username=request.user.username)
    carrito = CarritoCompras.objects.get(usuario=usuario, estado=False)
    plato = Plato.objects.get(id_plato=id_plato)
    
    elemento_carrito = ElementoCarrito.objects.filter(carrito=carrito, plato=plato)
    elemento_carrito.delete()
    
    return redirect('carrito')