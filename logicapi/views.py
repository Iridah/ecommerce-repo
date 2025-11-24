# # logicapi/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Importa la lógica de Python
from .logic import get_catalogo, get_carrito, calcular_total, agregar_al_carrito, vaciar_carrito as logic_vaciar_carrito

# Decorador para permitir peticiones POST sin el token CSRF (solo para API simple)
@csrf_exempt 
def catalogo_list(request):
    """Endpoint GET: Devuelve la lista de productos del catálogo."""
    catalogo = get_catalogo()
    # JsonResponse automáticamente convierte listas y diccionarios a JSON
    return JsonResponse({'success': True, 'catalogo': catalogo})

@csrf_exempt 
def carrito_view(request):
    """Endpoint GET: Devuelve el contenido del carrito y el total."""
    carrito = get_carrito()
    total = calcular_total()
    return JsonResponse({'success': True, 'carrito': carrito, 'total': total})

@csrf_exempt 
def agregar_producto(request):
    """Endpoint POST: Añade un producto al carrito."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body)
        producto_id = int(data.get('producto_id'))
        cantidad = int(data.get('cantidad', 1)) # Por defecto, cantidad es 1

        if agregar_al_carrito(producto_id, cantidad):
            return JsonResponse({'success': True, 'message': 'Producto agregado.'})
        else:
            return JsonResponse({'success': False, 'error': 'ID o cantidad inválida.'}, status=400)

    except (json.JSONDecodeError, ValueError):
        return JsonResponse({'success': False, 'error': 'Formato de datos JSON incorrecto.'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'error': f"Error interno: {str(e)}"}, status=500)

@csrf_exempt 
def vaciar_carrito(request):
    """Endpoint POST: Vacía el carrito."""
    if request.method == 'POST':
        logic_vaciar_carrito() # <--- ¡Llamada corregida y explícita!
        return JsonResponse({'success': True, 'message': 'Carrito vaciado.'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)