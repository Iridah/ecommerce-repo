# productos/admin.py

from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista del panel de admin
    list_display = ('nombre', 'slug', 'precio', 'stock', 'disponible', 'creado')
    # Filtros laterales
    list_filter = ('disponible', 'creado', 'actualizado')
    # Campos editables directamente en la lista
    list_editable = ('precio', 'stock', 'disponible')
    # Generar el slug automáticamente a partir del nombre
    prepopulated_fields = {'slug': ('nombre',)}