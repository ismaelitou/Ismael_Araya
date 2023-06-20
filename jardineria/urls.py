from django.urls import path
from .views import Inicio, Informacion, Catalogo, Contacto, Crear, Eliminar, Modificar

urlpatterns=[ 
    path('', Inicio, name="Inicio"),
    path('Informacion/', Informacion, name="Informacion"),
    path('Catalogo/', Catalogo, name="Catalogo"),
    path('Contacto/', Contacto, name="Contacto"),
    path('Crear/', Crear, name="Crear"),
    path('Eliminar/<id>/', Eliminar, name='Eliminar'),
    path('Modificar/<id>/', Modificar, name='Modificar'),
]