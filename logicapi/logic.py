# api/logic.py - Contiene toda la lógica del Ecommerce

# =======================================================================
# ESTRUCTURAS DE DATOS GLOBALES
# Usamos un único catálogo y carrito para simular la sesión (en un proyecto real, 
# el carrito estaría en la sesión o base de datos).
# =======================================================================

CATALOGO = [
    {'id': 1, 'nombre': 'Laptop Ultra', 'categoria': 'tecnologia', 'precio': 1200.00},
    {'id': 2, 'nombre': 'Teclado Mecánico', 'categoria': 'tecnologia', 'precio': 85.50},
    {'id': 3, 'nombre': 'Polera Algodón', 'categoria': 'ropa', 'precio': 25.00},
    {'id': 4, 'nombre': 'Juego de Sábanas', 'categoria': 'hogar', 'precio': 45.99},
    {'id': 5, 'nombre': 'Mouse Vertical', 'categoria': 'tecnologia', 'precio': 30.00},
]

# El carrito almacena {'producto_id': ID, 'nombre': 'nombre', 'cantidad': X, 'precio_unitario': Y}
CARRITO = [] 

# =======================================================================
# FUNCIONES (Requisito de Funciones, Ciclos y Condicionales)
# =======================================================================

def get_catalogo():
    """Devuelve la lista completa del catálogo."""
    return CATALOGO

def get_carrito():
    """Devuelve el contenido actual del carrito."""
    return CARRITO

def calcular_total():
    """Calcula la suma total del carrito (Sentencia Iterativa)."""
    total = 0.0
    for item in CARRITO:
        total += item['cantidad'] * item['precio_unitario']
    return total

def agregar_al_carrito(producto_id, cantidad):
    """Agrega una cantidad específica de un producto al carrito (Sentencia Condicional)."""
    producto_encontrado = next((p for p in CATALOGO if p['id'] == producto_id), None)
    
    if producto_encontrado and cantidad > 0:
        # Busca si el item ya existe en el carrito
        item_existente = next((item for item in CARRITO if item['producto_id'] == producto_id), None)
        
        if item_existente:
            item_existente['cantidad'] += cantidad
        else:
            CARRITO.append({
                'producto_id': producto_id,
                'nombre': producto_encontrado['nombre'],
                'cantidad': cantidad,
                'precio_unitario': producto_encontrado['precio']
            })
        return True
    return False

def vaciar_carrito():
    """Vacía el carrito por completo."""
    CARRITO.clear()
    return True