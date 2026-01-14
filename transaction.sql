-- Iniciamos la transacción para asegurar consistencia
BEGIN;

-- 1. Crear el encabezado del pedido para el usuario 3 (Pedro)
INSERT INTO pedidos (usuario_id, total) 
VALUES (3, 175.00); 

-- 2. Registrar el detalle: Pedro compra 1 Monitor (ID: 1) y 1 Mouse (ID: 2)
-- Usamos currval o una subconsulta para obtener el ID del pedido recién creado
INSERT INTO detalle_pedidos (pedido_id, producto_id, cantidad, precio_unitario)
VALUES 
(currval('pedidos_id_seq'), 1, 1, 150.00),
(currval('pedidos_id_seq'), 2, 1, 25.00);

-- 3. ACTUALIZAR EL STOCK (Crucial para el 120%)
UPDATE stock SET cantidad = cantidad - 1 WHERE producto_id = 1;
UPDATE stock SET cantidad = cantidad - 1 WHERE producto_id = 2;

-- Si todo salió bien, guardamos los cambios definitivamente
COMMIT;

-- En caso de error, usaríamos: ROLLBACK;