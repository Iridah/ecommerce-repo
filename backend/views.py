# backend/views.py
from django.shortcuts import render, get_object_or_404
from django.http import Http404 # Necesario para lanzar el error 404

# ===================================================
# SIMULACIÓN DE DATOS (Para que product_detail funcione)
# ===================================================
PRODUCTOS = [
    {'id': 1, 'nombre': 'Diseño Web Moderno', 'precio': 149.99, 'descripcion': 'Plantilla Bootstrap 5 optimizada para SEO.', 'imagen': 'producto1_placeholder.jpg', 'tecnologia': 'HTML, CSS, JS, Bootstrap', 'modulos': '3', 'escalabilidad': 'Alta', 'detalle_largo': 'Esta plantilla premium es ideal para portafolios.', 'caracteristicas': ['Diseño Responsivo', 'Optimización SEO', 'Soporte 24/7']},
    {'id': 2, 'nombre': 'Base de Datos con Python', 'precio': 99.50, 'descripcion': 'Servicio de migración y optimización de datos usando Python y SQL.', 'imagen': 'producto2_placeholder.jpg', 'tecnologia': 'Python, SQL, SQLAlchemy', 'modulos': '2', 'escalabilidad': 'Media', 'detalle_largo': 'Servicio enfocado en mejorar la eficiencia de la base de datos.', 'caracteristicas': ['Optimización de Queries', 'Migración de Esquemas', 'Pruebas de Carga']},
    {'id': 3, 'nombre': 'Script de Automatización', 'precio': 49.00, 'descripcion': 'Un microservicio en Python para tareas repetitivas de scraping o reportes.', 'imagen': 'producto3_placeholder.jpg', 'tecnologia': 'Python, Requests, Beautiful Soup', 'modulos': '1', 'escalabilidad': 'Baja', 'detalle_largo': 'Perfecto para automatizar la descarga de reportes diarios.', 'caracteristicas': ['Ejecución programada', 'Notificaciones por Email', 'Fácil Configuración']},
]

# ===================================================
# VISTAS
# ===================================================

def home(request):
    """
    Vista para la página de inicio (/)
    """
    # Renderiza el template 'index.html'
    return render(request, 'index.html', {})

def product_list(request):
    """
    Vista que renderiza el catálogo de productos (/productos)
    """
    context = {
        'productos': PRODUCTOS,
    }
    # Renderiza el template 'product_list.html'
    return render(request, 'product_list.html', context)

def product_detail(request, product_id):
    """
    Vista que renderiza la página de descripción de un producto específico.
    """
    # Busca el producto en la lista simulada
    producto = next((p for p in PRODUCTOS if p['id'] == product_id), None)
    
    # Si el producto no existe, lanza un error 404 (página no encontrada)
    if producto is None:
        raise Http404("Producto no encontrado.")

    context = {
        'producto': producto,
    }
    # Renderiza el template 'product_detail.html'
    return render(request, 'product_detail.html', context)