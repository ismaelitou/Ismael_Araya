from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def Inicio(request):
    return render(request, 'Inicio.html')

def Informacion(request):
    return render(request, 'Informacion.html')

def Contacto(request):
    return render(request, 'Contacto.html')

def Catalogo(request):
    productos = Producto.objects.raw('SELECT * FROM jardineria_producto')
    datos = {
        'productos': productos
    }
    return render(request, 'Catalogo.html', datos)

def Login(request):
    return render(request, "Login.html")

@login_required
def Crear(request):
    if request.method == 'POST':
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()
            return redirect('Catalogo')
    else:
        productoform = ProductoForm()
    return render(request, "Crear.html", {'productoform': productoform})

@login_required
def Eliminar(request, id):
    productoEliminado = Producto.objects.get(id=id)
    productoEliminado.delete()
    return redirect('Catalogo')

@login_required
def Modificar(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('Catalogo')
    return render(request, 'Modificar.html', datos)