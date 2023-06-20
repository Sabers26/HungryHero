from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Cliente)
admin.site.register(models.Plato)
admin.site.register(models.Carrito)