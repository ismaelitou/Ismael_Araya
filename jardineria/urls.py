from django.urls import path
from .views import Inicio, Informacion, Catalogo, Contacto, Crear, Eliminar, Modificar, Signin, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, CarritoCompras, generarBoleta

urlpatterns=[
    path('', Inicio, name="Inicio"),
    path('Informacion/', Informacion, name="Informacion"),
    path('Catalogo/', Catalogo, name="Catalogo"),
    path('Contacto/', Contacto, name="Contacto"),
    path('Crear/', Crear, name="Crear"),
    path('Carrito/', CarritoCompras, name="Carrito"),
    path('Eliminar/<id>/', Eliminar, name='Eliminar'),
    path('Modificar/<id>/', Modificar, name='Modificar'),
    path('Signin/', Signin, name="Signin"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]