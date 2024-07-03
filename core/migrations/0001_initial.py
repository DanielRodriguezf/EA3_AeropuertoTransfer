# Generated by Django 5.0.6 on 2024-06-29 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('rutChofer', models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut Chofer')),
                ('nombreChofer', models.CharField(max_length=40, verbose_name='Nombre Chofer')),
                ('apellidoChofer', models.CharField(max_length=40, verbose_name='Nombre Chofer')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('idEmpresa', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID Empresa')),
                ('nombreEmpresa', models.CharField(max_length=40, verbose_name='Nombre Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patenteVehiculo', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Id Vehiculo')),
                ('marca', models.CharField(max_length=40, verbose_name='Marca')),
                ('capacidad', models.IntegerField(max_length=10, verbose_name='Capacidad')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes', verbose_name='Imagen')),
                ('Chofer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.chofer', verbose_name='Chofer')),
                ('Empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empresa', verbose_name='Empresa')),
            ],
        ),
    ]
