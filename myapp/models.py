from django.db import models
from django.db.models import PROTECT, CASCADE
from django.contrib.auth.models import User, AbstractUser
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator, RegexValidator
# Create your models here.
validarLetras = RegexValidator(r'^[a-z  A-Z]*$', 'Ingrese solo letras')
# tablas necesarias para el retiro en tienda 
class Plato(models.Model):
    id_plato = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre_plato = models.TextField(unique=True, max_length=15, blank=False, null=False, validators=(MinValueValidator(1), MaxValueValidator(99999), validarLetras))
    precio_plato = models.BigIntegerField(null=False, validators=(MinValueValidator(1), MaxValueValidator(99999)), default=0)
    stock_plato = models.BigIntegerField(null=False, default=0, validators=(MinValueValidator(1), MaxValueValidator(99999)))
    activado = models.BooleanField(null=False, default=True)
    
    descripcion = models.TextField(null=False, blank=False, validators=(MinLengthValidator(1),MaxLengthValidator(100)))
                                         
    def __str__(self):
        return str(f'{self.nombre_plato}')
    

class Carrito(models.Model):
    id_carrito = models.UUIDField(primary_key=True, default=uuid.uuid4())
    id_plato = models.ForeignKey(Plato, on_delete=PROTECT)
    sub_total = models.BigIntegerField(null=False, default=0, validators=(MinValueValidator(1), MaxValueValidator(99999)))
    domicilio = models.TextField(null=False, blank=False, validators=(MinLengthValidator(5), MaxLengthValidator(100)))
    
    finalizado = models.BooleanField(null=False, default=False)

class Cliente(models.Model):
    id_cliente = models.UUIDField(primary_key=True)
    nombre = models.TextField(null=False, blank=False, validators=(MinLengthValidator(1), MaxLengthValidator(15), validarLetras))
    apellido = models.TextField(null=False, blank=False, validators=(MinLengthValidator(1), MaxLengthValidator(15), validarLetras))
    email = models.EmailField(null=False, blank=False, unique=True)
    
    cuenta = models.OneToOneField(User, unique=True, related_name='Perfil', on_delete=CASCADE)
    
    def __str__(self):
        return str(f'{self.email}')