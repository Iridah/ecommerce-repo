-- 1. Insertar Categorías (Mínimo 3 [cite: 37])
INSERT INTO categorias (nombre) VALUES 
('Electrónica'), 
('Hogar'), 
('Ropa');

-- 2. Insertar Usuarios (Mínimo 5, incluyendo Admin y tu rol de Coordinador [cite: 39])
INSERT INTO usuarios (username, password, rol) VALUES 
('admin_master', 'admin123', 'Admin'),
('ana_coord', 'coord456', 'Coordinador'), -- Tu plus del 20%
('juan_perez', 'user1', 'Cliente'),
('maria_g', 'user2', 'Cliente'),
('pedro_s', 'user3', 'Cliente');

-- 3. Insertar Productos (Mínimo 10 asociados a categorías [cite: 38])
-- Usaremos IDs 1, 2, 3 para las categorías creadas arriba
INSERT INTO productos (nombre, descripcion, precio, categoria_id) VALUES 
('Monitor 24"', 'Monitor Full HD', 150.00, 1),
('Mouse Gamer', 'Mouse RGB 3200 DPI', 25.00, 1),
('Teclado Mecánico', 'Switch Blue', 45.00, 1),
('Audífonos BT', 'Cancelación de ruido', 80.00, 1),
('Lámpara LED', 'Lámpara de escritorio', 15.00, 2),
('Silla Oficina', 'Ergonómica negra', 120.00, 2),
('Cafetera', 'Goteo 12 tazas', 35.00, 2),
('Camiseta Algodón', 'Talla L blanca', 10.00, 3),
('Jeans Slim', 'Denim azul', 30.00, 3),
('Polerón', 'Capucha gris', 25.00, 3);

-- 4. Insertar Stock inicial para cada producto [cite: 40]
-- Relacionamos el producto_id con la cantidad
INSERT INTO stock (producto_id, cantidad) VALUES 
(1, 10), (2, 50), (3, 30), (4, 20), (5, 15), 
(6, 5), (7, 12), (8, 100), (9, 40), (10, 25);