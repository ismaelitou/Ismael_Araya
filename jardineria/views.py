from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Boleta, Producto, detalle_boleta
from .forms import ProductoForm, RegistroForm
from django.core.paginator import Paginator
from django.http import Http404
from .compra import Carrito

#      - Templates -
def Inicio(request):
    return render(request, 'Inicio.html')
def Informacion(request):
    return render(request, 'Informacion.html')
def Contacto(request):
    return render(request, 'Contacto.html')
def Catalogo(request):
    productos = Producto.objects.raw('SELECT * FROM jardineria_producto')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 4)
        productos = paginator.page(page)
    except:
        raise Http404
    datos = {
        'productos': productos,
        'paginator': paginator
    }
    paginate_by = 2
    return render(request, 'Catalogo.html', datos)
def Login(request):
    return render(request, "login.html")
def Signin(request):
    data = {
        'form' : RegistroForm()
    }
    if request.method == 'POST':
        formulario = RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect('Inicio')
        data["form"] = formulario
    return render(request, 'registration/signin.html', data)
@login_required
def CarritoCompras(request):
    return render(request, 'Carrito.html')


#      - Funciones Administrador -
@login_required
def Crear(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            productoform = ProductoForm(request.POST, request.FILES)
            if productoform.is_valid():
                productoform.save()
                return redirect('Catalogo')
        else:
            productoform = ProductoForm()
        return render(request, "Crear.html", {'productoform': productoform})
    else:
        return redirect('Catalogo')
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


#      - Funciones Carrito -
@login_required
def agregar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito_compra.agregar(producto=producto)
    return redirect('Catalogo')
def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return redirect('Carrito')
def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(id = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'DetalleCarrito.html',datos)


#Sin implementar
def eliminar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito_compra.eliminar(producto=producto)
    return redirect("Catalogo")
def restar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito_compra.restar(producto=producto)
    return redirect("Catalogo")