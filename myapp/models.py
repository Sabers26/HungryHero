from django.db import models
from django.db.models import PROTECT, CASCADE
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

# tablas necesarias para el retiro en tienda
class Ingrediente(models.Model):
    id_ing = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre_ing = models.TextField(max_length=15, unique=True, blank=False, null=False)
    unidad_medida = models.TextField(null=False, blank=False, max_length=15)
    
    def __str__(self):
        return str(f'{self.nombre_ing}')
    
class Plato(models.Model):
    id_plato = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nombre_plato = models.TextField(unique=True, max_length=15, blank=False, null=False)
    
    def __str__(self):
        return str(f'{self.nombre_plato}')

class DetallePlato(models.Model):
    id_dPlato = models.UUIDField(primary_key=True, default=uuid.uuid4())
    id_plato = models.ForeignKey(Plato, on_delete=PROTECT)
    id_ingrediente = models.ForeignKey(Ingrediente, on_delete=PROTECT)
    cantidad = models.IntegerField(null=False, default=0, validators=(MinValueValidator(1), MaxValueValidator(9999)))
    