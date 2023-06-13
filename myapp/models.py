from django.db import models
from django.db.models import PROTECT, CASCADE
import uuid

# Create your models here.

# tablas necesarias para el retiro en tienda
class Ingrediente(models.Model):
    id_ing = models.TextField(primary_key=True, max_length=50)
    nombre_ing = models.TextField(max_length=15, unique=True, blank=False, null=False)
    
    UNIDAD = [
        ('ML', 'MILI LITROS'),
        ('GR', 'GRAMOS'),
        ('L', 'LITROS'),
        ('U', 'UNIDAD')
    ]
    
    unidad_medida = models.TextField(null=False, blank=False, choices=UNIDAD)
    
    def __str__(self):
        return str(f'{self.nombre_ing}')
    
class Plato(models.Model):
    id_plato = models.BigAutoField(primary_key=True)
    nombre_plato = models.TextField(unique=True, max_length=15, blank=False, null=False)
    
    def __str__(self):
        return str(f'{self.nombre_plato}')
