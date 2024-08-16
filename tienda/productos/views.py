from django.shortcuts import render, redirect
from .models import Cliente
from .models import Producto
from .forms import ProductoModelForm, ClienteModelForm
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def listar_clientes(request):
    clientes = Cliente.objects.all()

    return render(request, 'listar_clientes.html', {'clientes': clientes})

def listar_productos(request):
    query = request.GET.get('q')
    productos_list = Producto.objects.all()
    paginator = Paginator(productos_list, 10)
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')

    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)

    if precio_min and precio_max:
        productos_list = productos_list.filter(precio__gte=precio_min, precio__lte=precio_max)
    
    if query:
        productos_list = productos_list.filter(Q(nombre__icontains=query)| Q(descripcion__icontains=query))
    

    return render(request, 'listar_productos.html', {'productos': productos})

def inicio(request):
    return render(request, 'inicio.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoModelForm
    return render(request, 'agregar_producto.html', {'form': form})


def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteModelForm()
    return render(request, 'agregar_cliente.html', { 'form': form })