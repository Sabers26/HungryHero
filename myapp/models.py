from django.db import models
from django.db.models import PROTECT, CASCADE
from django.contrib.auth.models import User
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
# Create your models here.

# tablas necesarias para el retiro en tienda 
class Plato(models.Model):
    id_plato = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre_plato = models.TextField(unique=True, max_length=15, blank=False, null=False)
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
    
class Usuario(models.Model):
    nombre = models.TextField(null=False, blank=False, validators=((MinLengthValidator(1),MaxLengthValidator(30))))
    apellido = models.TextField(null=False, blank=False, validators=((MinLengthValidator(1),MaxLengthValidator(30))))
    usuario = models.OneToOneField(User, related_name='Perfil', on_delete=CASCADE)


    