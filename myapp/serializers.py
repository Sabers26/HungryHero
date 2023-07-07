from .models import *
from rest_framework import serializers

class PlatoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plato
        fields = ['id_plato', 'nombre_plato', 'stock_plato', 'precio_plato', ' estado_plato', 'descripcion', 'imagen']