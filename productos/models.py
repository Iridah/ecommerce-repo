# productos/models.py

from django.db import models

class Producto(models.Model):
    """
    Modelo de Base de Datos para los productos de la tienda.
    """
    # Información básica
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL Amigable") # Se usará para URLs limpias
    
    # Descripción y Precio
    descripcion_corta = models.TextField(verbose_name="Descripción Corta (Catálogo)")
    descripcion_larga = models.TextField(blank=True, verbose_name="Descripción Larga (Detalle)")
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    # Stock
    stock = models.IntegerField(default=0, verbose_name="Inventario")
    disponible = models.BooleanField(default=True)

    # Imagen (Requiere librerías adicionales en producción, pero aquí es un campo simple)
    # En un proyecto real, se usaría ImageField o FileField
    imagen = models.CharField(max_length=255, blank=True, verbose_name="Ruta o Nombre de Imagen")
    
    # Metadatos
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('nombre',)
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre

    # NOTA: En este punto podríamos añadir un método para obtener la URL, 
    # pero lo haremos cuando actualicemos las vistas.