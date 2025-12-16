from excepciones import CantidadInvalidaError, ProductoNoEncontradoError

class Producto:
    def __init__(self, id_prod, nombre, categoria, precio):
        self.id = id_prod
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)

    def __str__(self):
        return f"ID: {self.id} | {self.nombre} ({self.categoria}) | ${self.precio:.2f}"

class Usuario:
    def __init__(self, username):
        self.username = username
        self.rol = "Invitado"

class Cliente(Usuario):
    def __init__(self, username):
        super().__init__(username)
        self.rol = "Cliente"
        self.carrito = [] 

class Coordinador(Usuario):
    def __init__(self, username):
        super().__init__(username)
        self.rol = "Coordinador"

class Admin(Usuario):
    def __init__(self, username):
        super().__init__(username)
        self.rol = "Admin"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_por_id(self, id_prod):
        for p in self.productos:
            if p.id == id_prod:
                return p
        raise ProductoNoEncontradoError(id_prod)

    def listar_todo(self):
        if not self.productos:
            print("El catálogo está vacío.")
        for p in self.productos:
            print(p)

    def eliminar_producto(self, id_prod):
        producto = self.buscar_por_id(id_prod)
        self.productos.remove(producto)

class ItemCarrito:
    def __init__(self, producto, cantidad):
        if cantidad <= 0:
            raise CantidadInvalidaError(cantidad)
        self.producto = producto
        self.cantidad = cantidad

    def obtener_subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad} - Subtotal: ${self.obtener_subtotal():.2f}"