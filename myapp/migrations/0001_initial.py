# Generated by Django 4.2.2 on 2023-06-25 17:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id_plato', models.UUIDField(default=uuid.UUID('42647502-60ea-41f7-bd41-8d818ac7dd83'), primary_key=True, serialize=False)),
                ('nombre_plato', models.CharField(max_length=50, unique=True)),
                ('precio_plato', models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999)])),
                ('stock_plato', models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999)])),
                ('estado_plato', models.CharField(choices=[('HABILITADO', 'HABILITADO'), ('DESHABILITAD', 'DESHABILITADO')], default='HABILITADO', max_length=15)),
                ('descripcion', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(50)])),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.UUIDField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cuenta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_carrito', models.UUIDField(default=uuid.UUID('605b20c8-05be-4db1-b156-7a2521a9fa5a'), primary_key=True, serialize=False)),
                ('sub_total', models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999)])),
                ('domicilio', models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(80)])),
                ('finalizado', models.CharField(choices=[('FINALIZADO', 'FINALIZADO'), ('PENDIENTE', 'PENDIENTE')], default='PENDIENTE', max_length=15)),
                ('id_plato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.plato')),
            ],
        ),
    ]
