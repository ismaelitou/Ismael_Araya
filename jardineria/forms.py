from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'imagen']
        labels = {
            'id': 'ID',
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'stock': 'Stock',
            'imagen': 'Imagen'
        }
        widgets = {
            'id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ID del producto.',
                    'id': 'id',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre del producto.',
                    'id': 'nombre',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripción del producto.',
                    'id': 'descripcion',
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese precio del producto.',
                    'id': 'precio',
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese stock del producto.',
                    'id': 'stock',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese imagen del producto.',
                    'id': 'imagen',
                }
            ),
        }