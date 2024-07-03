from django.db import models
from distutils.command.upload import upload
import datetime

class Empresa(models.Model):
    idEmpresa = models.IntegerField(primary_key=True, verbose_name='ID Empresa')
    nombreEmpresa= models.CharField(max_length=40, verbose_name='Nombre Empresa')

    def __str__(self):
        return self.nombreEmpresa

class Chofer(models.Model):
    rutChofer = models.IntegerField(primary_key=True, verbose_name='Rut Chofer')
    nombreChofer = models.CharField(max_length=40, verbose_name='Nombre Chofer')
    apellidoChofer = models.CharField(max_length=40, verbose_name='Apellido Chofer')
    telefono = models.CharField(max_length=15, verbose_name='Teléfono')
    def __str__(self):
        return f"{self.nombreChofer} {self.apellidoChofer}"


class Vehiculo(models.Model):
    patenteVehiculo = models.CharField(primary_key=True, max_length=6, verbose_name='Patente Vehiculo')
    marca = models.CharField(max_length=40, verbose_name='Marca')
    capacidad = models.IntegerField(verbose_name='Capacidad')
    imagen = models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
    Chofer = models.ForeignKey('Chofer', on_delete=models.CASCADE, verbose_name='Chofer')
    Empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, verbose_name='Empresa')
    reservado = models.BooleanField(default=False, verbose_name='Reservado')

    def __str__(self):
        return self.patenteVehiculo


class Reserva(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name='Vehículo')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    rut = models.CharField(max_length=12, verbose_name='RUT')
    telefono = models.CharField(max_length=15, verbose_name='Teléfono')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    fecha_reserva = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Reserva')

    def __str__(self):
        return f'Reserva de {self.nombre} para {self.vehiculo.patenteVehiculo}'
