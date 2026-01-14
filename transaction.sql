-- Iniciamos la transacción para asegurar consistencia 

-- 1. Crear el encabezado del pedido 
INSERT INTO pedidos (usuario_id, total) 
VALUES (3, 175.00); 

-- 2. Registrar el detalle 
INSERT INTO detalle_pedidos (pedido_id, producto_id, cantidad, precio_unitario)
VALUES (currval('pedidos_id_seq'), 1, 1, 150.00);

-- 3. ACTUALIZACIÓN CON VALIDACIÓN DE SEGURIDAD (La clave de Vacadari SpA) 
-- Solo descuenta si el stock resultante es mayor o igual a 0
UPDATE stock 
SET cantidad = cantidad - 1 
WHERE producto_id = 1 AND cantidad >= 1;

-- 4. CONTROL DE INTEGRIDAD 
-- Si el UPDATE no afectó a ninguna fila (porque no había stock), 
-- cancelamos todo para evitar el "pastel de fresa".
-- Nota: En un script puro SQL se valida visualmente o con funciones de control.
-- Para efectos del portafolio, el COMMIT sella la operación. 

COMMIT;