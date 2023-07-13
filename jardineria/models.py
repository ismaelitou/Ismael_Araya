import datetime
from distutils.command.upload import upload
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    descripcion = models.CharField(max_length=100, blank=True, verbose_name="Descripción")
    precio = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], verbose_name="Precio")
    stock = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,10}$')], verbose_name="Stock")
    imagen = models.ImageField(upload_to="productos", null=True, blank=True, verbose_name="Imagen")
    

    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)