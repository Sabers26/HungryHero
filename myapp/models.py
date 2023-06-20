from django.db import models
from django.db.models import PROTECT, CASCADE
from django.contrib.auth.models import User, AbstractUser
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
# Create your models here.
# tablas necesarias para el retiro en tienda 
class Plato(models.Model):
    id_plato = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre_plato=models.CharField(max_length=50, null=False, unique=True, blank=False)
    precio_plato = models.BigIntegerField(null=False, validators=(MinValueValidator(1), MaxValueValidator(99999)), default=0)
    stock_plato = models.BigIntegerField(null=False, default=0, validators=(MinValueValidator(1), MaxValueValidator(99999)))
    
    ESTADO = [
        ('HABILITADO', 'HABILITADO'),
        ('DESHABILITAD', 'DESHABILITADO')
    ]
    estado_plato = models.CharField(null=False, default="HABILITADO", max_length=15, choices=ESTADO)
    
    descripcion = models.TextField(null=False, validators=(MinLengthValidator(1), MaxLengthValidator(300)))
    
    # imagen = models.ImageField(null=False)
    def __str__(self):
        return str(f'{self.nombre_plato}')
    

class Carrito(models.Model):
    id_carrito = models.UUIDField(primary_key=True, default=uuid.uuid4())
    id_plato = models.ForeignKey(Plato, on_delete=PROTECT)
    sub_total = models.BigIntegerField(null=False, default=0, validators=(MinValueValidator(1), MaxValueValidator(99999)))
    domicilio = models.TextField(null=False, blank=False, validators=(MinLengthValidator(5), MaxLengthValidator(300)))
    
    ESTADO = [
        ('FINALIZADO', 'FINALIZADO'),
        ('PENDIENTE', 'PENDIENTE')
    ]
    
    finalizado = models.CharField(null=False, default="PENDIENTE", max_length=15, choices=ESTADO)

class Cliente(models.Model):
    id_cliente = models.UUIDField(primary_key=True)
    nombre = models.CharField(null=False, blank=False, max_length=20)
    apellido = models.CharField(null=False, blank=False, max_length=20)
    email = models.EmailField(null=False, blank=False, unique=True)
    
    cuenta = models.OneToOneField(User, unique=True, related_name='Perfil', on_delete=CASCADE)
    
    def __str__(self):
        return str(f'{self.email}')