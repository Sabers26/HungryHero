# Generated by Django 4.2.2 on 2023-06-20 00:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_plato_activado_plato_finalizado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plato',
            old_name='finalizado',
            new_name='estado_plato',
        ),
        migrations.AlterField(
            model_name='carrito',
            name='id_carrito',
            field=models.UUIDField(default=uuid.UUID('65aef58c-c9ed-40c8-8714-5e35317b7b47'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plato',
            name='id_plato',
            field=models.UUIDField(default=uuid.UUID('f2619760-dffb-42ce-b6b1-536d7d692f4a'), primary_key=True, serialize=False),
        ),
    ]
