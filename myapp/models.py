from django.db import models
from django.db.models import PROTECT, CASCADE
from django.contrib.auth.models import User, AbstractUser
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
# Create your models here.
# tablas necesarias para el retiro en tienda 
class Plato(models.Model):
    id_plato = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre_plato=models.CharField(max_length=50, null=False, unique=True, blank=False)
    precio_plato = models.BigIntegerField(null=False, validators=(MinValueValidator(1), MaxValueValidator(99999)), default=0)
    stock_plato = models.BigIntegerField(null=False, default=0, validators=(MinValueValidator(1), MaxValueValidator(99999)))
    
    ESTADO = [
        ('HABILITADO', 'HABILITADO'),
        ('DESHABILITAD', 'DESHABILITADO')
    ]
    estado_plato = models.CharField(null=False, default="HABILITADO", max_length=15, choices=ESTADO)
    
    descripcion = models.CharField(null=False, max_length=50, validators=(MinLengthValidator(1), MaxLengthValidator(50)))
    
    imagen = models.CharField(unique=True, null=False, max_length= 500, default='Sin imagen')
    def __str__(self):
        return str(f'{self.nombre_plato}')
    

class CarritoCompras(models.Model):
    id_carrito = models.UUIDField(primary_key=True, default=uuid.uuid4())
    platos = models.ManyToManyField(Plato, through='ElementoCarrito')
    total_venta = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    usuario = models.ForeignKey(User, on_delete=PROTECT)
    estado = models.BooleanField(default=False)
    
    def actualizar_total(self):
        self.total_venta = sum(elemento.sub_total for elemento in self.elementocarrito_set.all()) #esperamos a terminar la otra tabla
        self.save()
        
    def __str__(self):
        return str(f'carrito de {self.usuario.username} - {self.estado}')

class ElementoCarrito(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=PROTECT)
    plato = models.ForeignKey(Plato, on_delete=PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    sub_total = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return str(f'elementos del carrito de {self.carrito.usuario.username}')
    
    def calcular_subTotal(self):
        self.sub_total = self.cantidad*self.plato.precio_plato
        self.save()

class Cliente(models.Model):
    id_cliente = models.UUIDField(primary_key=True)
    nombre = models.CharField(null=False, blank=False, max_length=20)
    apellido = models.CharField(null=False, blank=False, max_length=20)
    email = models.EmailField(null=False, blank=False, unique=True)
    
    cuenta = models.OneToOneField(User, unique=True, related_name='Perfil', on_delete=PROTECT)
    
    def __str__(self):
        return str(f'{self.email}')