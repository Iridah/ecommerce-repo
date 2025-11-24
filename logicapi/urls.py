# logicapi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 1. Obtener el Catálogo y Carrito
    path('catalogo/', views.catalogo_list, name='api_catalogo_list'), # GET para la lista de productos
    path('carrito/', views.carrito_view, name='api_carrito_view'),     # GET para el carrito
    
    # 2. Modificación del Carrito
    path('carrito/agregar/', views.agregar_producto, name='api_agregar_producto'), # POST
    path('carrito/vaciar/', views.vaciar_carrito, name='api_vaciar_carrito'),     # POST
]