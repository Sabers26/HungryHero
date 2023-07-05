# Generated by Django 4.2.2 on 2023-07-05 02:40

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
            name='CarritoCompras',
            fields=[
                ('id_carrito', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('total_venta', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id_plato', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nombre_plato', models.CharField(max_length=50, unique=True)),
                ('precio_plato', models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999)])),
                ('stock_plato', models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999)])),
                ('estado_plato', models.CharField(choices=[('HABILITADO', 'HABILITADO'), ('DESHABILITAD', 'DESHABILITADO')], default='HABILITADO', max_length=15)),
                ('descripcion', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(50)])),
                ('imagen', models.CharField(default='Sin imagen', max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElementoCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.carritocompras')),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.plato')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.UUIDField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cuenta', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='Perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='carritocompras',
            name='platos',
            field=models.ManyToManyField(through='myapp.ElementoCarrito', to='myapp.plato'),
        ),
        migrations.AddField(
            model_name='carritocompras',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
