from django.urls import path
from .views import listar_clientes, listar_productos, agregar_producto, agregar_cliente

urlpatterns = [
    path('clientes/', listar_clientes, name='listar_clientes'),
    path('productos/', listar_productos, name='listar_productos'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('agregar_cliente/', agregar_cliente, name='agregar_cliente'),
]