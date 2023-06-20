# Generated by Django 4.2.2 on 2023-06-20 00:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_carrito_domicilio_alter_carrito_id_carrito_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='finalizado',
            field=models.CharField(choices=[('HABILITADO', 'HABILITADO'), ('DESHABILITAD', 'DESHABILITAD')], default='HABILITADO', max_length=15),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='id_carrito',
            field=models.UUIDField(default=uuid.UUID('c215235c-e09c-4621-9835-aec5281d8530'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plato',
            name='id_plato',
            field=models.UUIDField(default=uuid.UUID('80d7ff9b-a559-4e84-8655-e2c493da2492'), primary_key=True, serialize=False),
        ),
    ]