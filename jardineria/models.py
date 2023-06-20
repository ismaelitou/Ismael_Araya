from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

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