# ecommerce_m3.py
# Archivo de Entrega Oficial - E-commerce CLI Módulo 3

# =======================================================================
# 1. ESTRUCTURAS DE DATOS INICIALES (Requisito de Estructuras de Datos)
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
# 2. FUNCIONES (Requisito de Funciones)
# =======================================================================

def mostrar_catalogo(catalogo):
    """Muestra todos los productos del catálogo (Ciclo for)."""
    print("\n--- Catálogo de Productos ---")
    for producto in catalogo:
        # Usa snake_case y formatos requeridos
        print(f"ID: {producto['id']} | {producto['nombre']} ({producto['categoria'].capitalize()}) | ${producto['precio']:.2f}")
    print("-----------------------------\n")

def buscar_producto(consulta):
    """Busca productos por nombre o categoría (Condicional y Ciclo)."""
    resultados = []
    consulta = consulta.lower()
    for prod in CATALOGO:
        if consulta in prod['nombre'].lower() or consulta in prod['categoria'].lower():
            resultados.append(prod)
    return resultados # Retorna un valor (cumpliendo requisito)

def agregar_al_carrito(producto_id, cantidad):
    """Agrega un producto validando ID y cantidad (Condicionales)."""
    producto_encontrado = next((p for p in CATALOGO if p['id'] == producto_id), None)
    
    # Validar que el ID exista [cite: 43] y que la cantidad sea > 0 [cite: 68]
    if producto_encontrado and cantidad > 0:
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

def calcular_total():
    """Calcula la suma total del carrito (Ciclo for)."""
    total = 0.0
    for item in CARRITO:
        total += item['cantidad'] * item['precio_unitario']
    return total # Retorna un valor (cumpliendo requisito)

def mostrar_carrito_y_total():
    """Muestra el contenido actual del carrito (Opción 4)."""
    if not CARRITO: # Condicional: Carrito vacío [cite: 69]
        print("\nEl carrito está vacío.")
        return

    print("\n--- Tu Carrito de Compras ---")
    # Listar ítems con ID, nombre, cantidad, precio unitario, subtotal [cite: 48]
    for item in CARRITO:
        subtotal = item['cantidad'] * item['precio_unitario']
        print(f"ID: {item['producto_id']} | {item['nombre']} x{item['cantidad']} @ ${item['precio_unitario']:.2f} = Subtotal: ${subtotal:.2f}")

    total = calcular_total()
    print("-----------------------------")
    print(f"TOTAL A PAGAR: ${total:.2f}") # Mostrar total a pagar [cite: 49]
    print("-----------------------------\n")

def vaciar_carrito():
    """Vacía el carrito (Opción 5)."""
    CARRITO.clear()
    print("El carrito ha sido vaciado.") # Mensaje de confirmación [cite: 51]


# =======================================================================
# 3. MENÚ PRINCIPAL (Punto de Entrada CLI)
# =======================================================================

def menu_principal():
    """Maneja el flujo principal del programa."""
    print("Bienvenido/a a tu Ecommerce")
    
    while True: # Ciclo while para el menú [cite: 71]
        print("\n--- Menú Principal ---")
        print("1) Ver catálogo de productos")
        print("2) Buscar producto por nombre o categoría")
        print("3) Agregar producto al carrito")
        print("4) Ver carrito y total")
        print("5) Vaciar carrito")
        print("0) Salir")
        
        opcion = input("Seleccione una opción: ")
        
        # Sentencias Condicionales para opciones del menú [cite: 65, 66]
        if opcion == '1':
            mostrar_catalogo(CATALOGO)
            
        elif opcion == '2':
            consulta = input("Ingrese nombre o categoría a buscar: ")
            resultados = buscar_producto(consulta)
            if resultados:
                mostrar_catalogo(resultados)
            else:
                print(f"No se encontraron productos para '{consulta}'.")
                
        elif opcion == '3':
            try:
                producto_id = int(input("Ingrese el ID del producto a agregar: "))
                cantidad = int(input("Ingrese la cantidad: "))
                
                if agregar_al_carrito(producto_id, cantidad):
                    print(f"Producto ID {producto_id} agregado al carrito.")
                else:
                    print("Error: ID de producto no válido o cantidad menor a 1.")
            except ValueError:
                print("Error: Por favor, ingrese un ID y una cantidad válidos (números enteros).")
                
        elif opcion == '4':
            mostrar_carrito_y_total()

        elif opcion == '5':
            vaciar_carrito()
            
        elif opcion == '0':
            print("Gracias por su compra. ¡Hasta pronto!")
            break # Sale del ciclo while
            
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()