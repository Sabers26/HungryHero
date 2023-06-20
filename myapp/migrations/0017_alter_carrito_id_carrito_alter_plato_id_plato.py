# Generated by Django 4.2.2 on 2023-06-20 18:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_carrito_id_carrito_alter_plato_id_plato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='id_carrito',
            field=models.UUIDField(default=uuid.UUID('eb3ae9ae-3190-478c-b31d-c3e67daa8639'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plato',
            name='id_plato',
            field=models.UUIDField(default=uuid.UUID('20a988ea-a22a-40a0-ae8c-e66f8467df4d'), primary_key=True, serialize=False),
        ),
    ]
