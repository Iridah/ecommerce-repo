class EcommerceError(Exception):
    """Clase base para otras excepciones de esta aplicación."""
    pass

class ProductoNoEncontradoError(EcommerceError):
    def __init__(self, producto_id, mensaje="El producto con ID {} no existe."):
        self.producto_id = producto_id
        self.mensaje = mensaje.format(producto_id)
        super().__init__(self.mensaje)

class CantidadInvalidaError(EcommerceError):
    def __init__(self, cantidad, mensaje="La cantidad '{}' no es válida. Debe ser mayor a 0."):
        self.cantidad = cantidad
        self.mensaje = mensaje.format(cantidad)
        super().__init__(self.mensaje)

class ArchivoError(EcommerceError):
    pass