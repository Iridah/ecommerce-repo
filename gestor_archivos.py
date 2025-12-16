import os

class GestorArchivos:
    @staticmethod
    def guardar_catalogo(nombre_archivo, productos):
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                for p in productos:
                    # Guardamos ID, Nombre, Categoria, Precio
                    f.write(f"{p.id},{p.nombre},{p.categoria},{p.precio}\n")
        except Exception as e:
            print(f"Error al guardar catálogo: {e}")

    @staticmethod
    def cargar_catalogo(nombre_archivo):
        """Retorna una lista de listas con los datos crudos."""
        datos_crudos = []
        if not os.path.exists(nombre_archivo):
            return datos_crudos
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) == 4:
                        datos_crudos.append(partes)
        except Exception as e:
            print(f"Error al cargar catálogo: {e}")
        return datos_crudos

    @staticmethod
    def registrar_orden(nombre_archivo, username, items, total):
        from datetime import datetime
        try:
            with open(nombre_archivo, 'a', encoding='utf-8') as f:
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"--- Orden de {username} | Fecha: {fecha} ---\n")
                for item in items:
                    f.write(f"  - {item}\n")
                f.write(f"TOTAL: ${total:.2f}\n")
                f.write("-" * 40 + "\n")
        except Exception as e:
            print(f"Error al registrar orden: {e}")