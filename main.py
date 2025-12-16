# type: ignore
import time
import os
from clases import Producto, Catalogo, Admin, Cliente, Coordinador, ItemCarrito
from gestor_archivos import GestorArchivos
from excepciones import EcommerceError

# Configuración y Colores
ARCHIVO_CATALOGO = "catalogo.txt"
ARCHIVO_ORDENES = "ordenes.txt"
COLOR_HEADER = "\033[95m"
COLOR_INFO = "\033[94m"
COLOR_EXITO = "\033[92m"
COLOR_AVISO = "\033[93m"
COLOR_ERROR = "\033[91m"
COLOR_RESET = "\033[0m"

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_error(mensaje):
    print(f"\n{COLOR_ERROR}❌ ERROR: {mensaje}{COLOR_RESET}")
    time.sleep(2)

def mostrar_exito(mensaje):
    print(f"\n{COLOR_EXITO}✅ ÉXITO: {mensaje}{COLOR_RESET}")
    time.sleep(1.5)

# --- MENÚS ---
def menu_admin(usuario, catalogo):
    while True:
        limpiar_pantalla()
        print(f"{COLOR_HEADER}--- PANEL ADMIN (Usuario: {usuario.username}) ---{COLOR_RESET}")
        print("1. Listar productos\n2. Agregar producto\n3. Eliminar producto\n4. Guardar en archivo\n0. Salir")
        opc = input(f"\n{COLOR_INFO}Seleccione: {COLOR_RESET}")
        
        if opc == "1":
            catalogo.listar_todo()
            input(f"\n{COLOR_AVISO}Presione Enter para continuar...{COLOR_RESET}")
        elif opc == "2":
            try:
                id_p = int(input("ID: "))
                nom, cat = input("Nombre: "), input("Categoría: ")
                pre = float(input("Precio: "))
                catalogo.agregar_producto(Producto(id_p, nom, cat, pre))
                mostrar_exito("Producto añadido temporalmente.")
            except ValueError: mostrar_error("Datos numéricos inválidos.")
        elif opc == "3":
            try:
                id_p = int(input("ID a eliminar: "))
                catalogo.eliminar_producto(id_p)
                mostrar_exito("Producto eliminado.")
            except EcommerceError as e: mostrar_error(e)
        elif opc == "4":
            GestorArchivos.guardar_catalogo(ARCHIVO_CATALOGO, catalogo.productos)
            mostrar_exito("Cambios persistidos en el disco.")
        elif opc == "0": break
        else: mostrar_error(f"'{opc}' no es una opción válida.")

def menu_coordinador(usuario, catalogo):
    while True:
        limpiar_pantalla()
        print(f"{COLOR_HEADER}--- PANEL COORDINACIÓN (Usuario: {usuario.username}) ---{COLOR_RESET}")
        print("1. Ver Inventario\n2. Ver Registro de Ventas\n0. Salir")
        opc = input(f"\n{COLOR_INFO}Seleccione: {COLOR_RESET}")
        
        if opc == "1":
            catalogo.listar_todo()
            input(f"\n{COLOR_AVISO}Presione Enter para continuar...{COLOR_RESET}")
        elif opc == "2":
            if os.path.exists(ARCHIVO_ORDENES):
                with open(ARCHIVO_ORDENES, 'r', encoding='utf-8') as f: print(f.read())
                input(f"\n{COLOR_AVISO}Presione Enter para continuar...{COLOR_RESET}")
            else: mostrar_error("No hay registros de órdenes.")
        elif opc == "0": break
        else: mostrar_error(f"'{opc}' no es una opción válida.")

def menu_cliente(usuario, catalogo):
    carrito = []
    while True:
        limpiar_pantalla()
        print(f"{COLOR_HEADER}--- TIENDA (Cliente: {usuario.username}) ---{COLOR_RESET}")
        print("1. Ver catálogo\n2. Agregar al carrito\n3. Ver carrito\n4. Pagar\n0. Salir")
        opc = input(f"\n{COLOR_INFO}Seleccione: {COLOR_RESET}")
        
        if opc == "1":
            catalogo.listar_todo()
            input(f"\n{COLOR_AVISO}Presione Enter para continuar...{COLOR_RESET}")
        elif opc == "2":
            try:
                id_p = int(input("ID: "))
                prod = catalogo.buscar_por_id(id_p)
                cant = int(input("Cantidad: "))
                carrito.append(ItemCarrito(prod, cant))
                mostrar_exito("Agregado al carrito.")
            except EcommerceError as e: mostrar_error(e)
            except ValueError: mostrar_error("Ingrese números válidos.")
        elif opc == "3":
            if not carrito: mostrar_error("Carrito vacío.")
            else:
                total = sum(i.obtener_subtotal() for i in carrito)
                for i in carrito: print(i)
                print(f"TOTAL: ${total:.2f}")
                input(f"\n{COLOR_AVISO}Presione Enter...{COLOR_RESET}")
        elif opc == "4":
            if not carrito: mostrar_error("El carrito está vacío.")
            else:
                total = sum(i.obtener_subtotal() for i in carrito)
                GestorArchivos.registrar_orden(ARCHIVO_ORDENES, usuario.username, carrito, total)
                mostrar_exito("¡Compra realizada! Ticket generado.")
                carrito = []
        elif opc == "0": break
        else: mostrar_error(f"'{opc}' no es una opción válida.")

def main():
    try:
        limpiar_pantalla()
        catalogo = Catalogo()
        
        # Carga de datos inicial
        datos_crudos = GestorArchivos.cargar_catalogo(ARCHIVO_CATALOGO)
        for d in datos_crudos:
            # Re-instanciamos los objetos Producto usando los datos del archivo
            p = Producto(int(d[0]), d[1], d[2], float(d[3]))
            catalogo.agregar_producto(p)
        
        print(f"{COLOR_HEADER}=== SISTEMA ECOMMERCE POO 120% ==={COLOR_RESET}")
        user = input("Ingrese su nombre: ")
        print("Roles disponibles: 1. Admin | 2. Coordinador | 3. Cliente")
        rol_opc = input("Seleccione su rol: ")

        if rol_opc == "1":
            menu_admin(Admin(user), catalogo)
        elif rol_opc == "2":
            menu_coordinador(Coordinador(user), catalogo)
        else:
            menu_cliente(Cliente(user), catalogo)
            
    except Exception as e:
        print(f"\n\033[91m⚠️ ERROR CRÍTICO AL INICIAR: {e}\033[0m")

if __name__ == "__main__":
    main()