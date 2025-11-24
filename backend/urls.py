# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 
# NOTA: Si views.home y views.product_list están en la app 'backend', 
# la línea 'from . import views' es correcta.
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls), 

    # RUTA 1: INICIO (Landing Page - Asumo que usa templates/index.html)
    path('', views.home, name='home'), 
    
    # RUTA 2: CATÁLOGO FUNCIONAL (Donde corre el JavaScript y la API)
    # Servirá el template product_list.html (con el nuevo contenido)
    path('productos/', TemplateView.as_view(template_name='product_list.html'), name='product_list'), 
    
    # RUTA 3: DETALLE DE PRODUCTO (Si aún quieres mantenerla)
    path('productos/<int:product_id>/', views.product_detail, name='product_detail'), 
    
    # RUTA CRUCIAL 4: CONEXIÓN CON LA API
    # Redirige todo el tráfico que empieza con /api/ a la aplicación logicapi
    path('api/', include('logicapi.urls')), # <--- ¡ESTO CONECTA EL JS CON PYTHON!
]