# Generated by Django 4.2.2 on 2023-06-19 22:24

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_carrito_id_carrito_alter_cliente_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='id_carrito',
            field=models.UUIDField(default=uuid.UUID('eb54cdc4-3c83-4f71-8316-c3a9195b9910'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plato',
            name='descripcion',
            field=models.TextField(validators=[django.core.validators.RegexValidator('^[a-z A-Z]*$', 'Ingrese solo letras')]),
        ),
        migrations.AlterField(
            model_name='plato',
            name='id_plato',
            field=models.UUIDField(default=uuid.UUID('8019cc5a-d6f6-4312-91ea-de8aa9edff0c'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plato',
            name='nombre_plato',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
