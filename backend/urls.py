# backend/urls.py

from django.contrib import admin
from django.urls import path
from . import views 

# Cambié la variable urlsPatterns a urlpatterns, que es la convención estándar
urlpatterns = [
    path('admin/', admin.site.urls), 

    # RUTA DE INICIO
    path('', views.home, name='home'), 
    
    # RUTA DEL CATÁLOGO (Listado)
    path('productos/', views.product_list, name='product_list'), 
    
    # RUTA DEL DETALLE (FINAL)
    # Esta ruta captura un entero llamado 'product_id'
    path('productos/<int:product_id>/', views.product_detail, name='product_detail'), 
    
    # PLACEHOLDERS
    # path('carrito/', views.product_list, name='cart'), 
    # path('login/', views.product_list, name='login'),
]