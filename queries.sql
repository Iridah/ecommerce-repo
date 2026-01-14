-- 1. Listar todos los productos junto a su categoría
SELECT p.nombre, p.precio, c.nombre AS categoria
FROM productos p
JOIN categorias c ON p.categoria_id = c.id;

-- 2. Buscar productos por nombre (ejemplo con 'Monitor')
SELECT * FROM productos WHERE nombre LIKE '%Monitor%';

-- 3. Filtrar productos por categoría (ejemplo con categoría 1 - Electrónica)
SELECT * FROM productos WHERE categoria_id = 1;

-- 4. Identificar productos con stock bajo (menos de 10 unidades)
-- Este es un plus para la gestión de inventario
SELECT p.nombre, s.cantidad
FROM productos p
JOIN stock s ON p.id = s.producto_id
WHERE s.cantidad < 10;