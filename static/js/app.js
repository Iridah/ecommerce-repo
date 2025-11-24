// static/js/app.js

document.addEventListener('DOMContentLoaded', () => {
    // 1. Captura de elementos del DOM
    const catalogoContainer = document.getElementById('catalogo-productos');
    const carritoContainer = document.getElementById('carrito-detalle');
    const totalMonto = document.getElementById('total-monto');
    const btnVaciar = document.getElementById('btn-vaciar');

    // 2. Event Listeners
    btnVaciar.addEventListener('click', vaciarCarrito);
    
    // Inicializar: Cargar el catálogo y el carrito al iniciar
    cargarCatalogo();
    cargarCarrito();

    // =========================================================================
    // FUNCIONES DE COMUNICACIÓN CON LA API DE DJANGO (Backend)
    // =========================================================================

    /**
     * Hace una petición GET a la API para obtener el catálogo de productos.
     */
    async function cargarCatalogo() {
        try {
            // Petición GET al endpoint de Django /api/catalogo/
            const response = await fetch('/api/catalogo/'); 
            
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }

            const data = await response.json();
            mostrarCatalogoEnHTML(data.catalogo);

        } catch (error) {
            console.error('Error al cargar el catálogo:', error);
            catalogoContainer.innerHTML = `<p class="text-danger">Error: No se pudo conectar con el servidor backend (API).</p>`;
        }
    }

    /**
     * Muestra el catálogo de productos en la interfaz web.
     * @param {Array} catalogo Lista de objetos producto.
     */
    function mostrarCatalogoEnHTML(catalogo) {
        catalogoContainer.innerHTML = '';
        if (catalogo.length === 0) {
            catalogoContainer.innerHTML = `<p class="text-muted">No hay productos en el catálogo.</p>`;
            return;
        }

        catalogo.forEach(producto => {
            const card = document.createElement('div');
            card.className = 'col';
            card.innerHTML = `
                <div class="card h-100 shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title text-primary">${producto.nombre}</h5>
                        <p class="card-text mb-1">Categoría: <span class="badge bg-secondary">${producto.categoria}</span></p>
                        <h4 class="text-success">$${producto.precio.toFixed(2)}</h4>
                        <button class="btn btn-sm btn-primary btn-add-carrito" data-id="${producto.id}">
                            + Agregar al carrito
                        </button>
                    </div>
                </div>
            `;
            catalogoContainer.appendChild(card);
        });
        
        // Agregar Event Listener a todos los nuevos botones "Agregar al Carrito"
        document.querySelectorAll('.btn-add-carrito').forEach(button => {
            button.addEventListener('click', (e) => {
                const productoId = parseInt(e.target.dataset.id);
                agregarAlCarritoAPI(productoId);
            });
        });
    }

    /**
     * Hace una petición POST a la API para añadir un producto al carrito.
     * @param {number} id ID del producto.
     */
    async function agregarAlCarritoAPI(id) {
        try {
            const response = await fetch('/api/carrito/agregar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // En Django real: 'X-CSRFToken': obtenerCookie('csrftoken')
                },
                body: JSON.stringify({ producto_id: id, cantidad: 1 })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Error al agregar producto.');
            }

            alert('Producto añadido al carrito.');
            cargarCarrito(); // Recargar el carrito para mostrar el cambio

        } catch (error) {
            console.error('Error al agregar al carrito:', error);
            alert(`Fallo al añadir: ${error.message}`);
        }
    }

    /**
     * Hace una petición GET a la API para obtener el contenido actual del carrito.
     */
    async function cargarCarrito() {
        try {
            const response = await fetch('/api/carrito/');
            const data = await response.json();
            
            mostrarCarritoEnHTML(data.carrito, data.total);
        } catch (error) {
            console.error('Error al cargar el carrito:', error);
            mostrarCarritoEnHTML([], 0); // Mostrar vacío en caso de error
        }
    }

    /**
     * Muestra el contenido del carrito y el total en la interfaz.
     * @param {Array} carrito Lista de ítems en el carrito.
     * @param {number} total Monto total a pagar.
     */
    function mostrarCarritoEnHTML(carrito, total) {
        carritoContainer.innerHTML = '';
        document.getElementById('empty-carrito')?.remove();
        
        if (carrito.length === 0) {
            carritoContainer.innerHTML = `<p id="empty-carrito" class="text-muted">El carrito está vacío. ¡Agrega productos!</p>`;
        } else {
            carrito.forEach(item => {
                const subtotal = item.cantidad * item.precio_unitario;
                const li = document.createElement('div');
                li.className = 'list-group-item d-flex justify-content-between align-items-center';
                li.innerHTML = `
                    <span>${item.nombre} x${item.cantidad}</span>
                    <span class="text-info">$${subtotal.toFixed(2)}</span>
                `;
                carritoContainer.appendChild(li);
            });
        }
        
        totalMonto.textContent = `$${total.toFixed(2)}`;
    }

    /**
     * Hace una petición POST a la API para vaciar el carrito.
     */
    async function vaciarCarrito() {
        if (!confirm('¿Está seguro de que desea vaciar el carrito?')) return;

        try {
            const response = await fetch('/api/carrito/vaciar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({})
            });

            if (!response.ok) {
                 throw new Error('Fallo en la API al vaciar el carrito.');
            }

            alert('Carrito vaciado exitosamente.');
            cargarCarrito(); 

        } catch (error) {
            console.error('Error al vaciar el carrito:', error);
            alert(`Fallo al vaciar el carrito: ${error.message}`);
        }
    }

});