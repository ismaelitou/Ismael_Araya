from django.contrib import admin
from .models import Boleta, Producto, detalle_boleta

# Register your models here.
admin.site.register(Producto)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)