-- 1. Creación de la base de datos (Opcional dependiendo de tu gestor)
-- CREATE DATABASE ecommerce_db;

-- 2. Tabla de Categorías
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- 3. Tabla de Usuarios (Incluyendo tu rol de Coordinador)
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL, -- En un sistema real iría encriptado
    rol VARCHAR(20) NOT NULL CHECK (rol IN ('Admin', 'Coordinador', 'Cliente')) 
);

-- 4. Tabla de Productos
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL CHECK (precio > 0), -- Validación de precio 
    categoria_id INTEGER REFERENCES categorias(id) ON DELETE SET NULL
);

-- 5. Tabla de Stock (Entidad separada para mejor control)
CREATE TABLE stock (
    producto_id INTEGER PRIMARY KEY REFERENCES productos(id) ON DELETE CASCADE,
    cantidad INTEGER NOT NULL CHECK (cantidad >= 0) -- No permite stock negativo 
);

-- 6. Tabla de Pedidos
CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) DEFAULT 0
);

-- 7. Detalle de Pedidos (Relación muchos a muchos entre Pedidos y Productos)
CREATE TABLE detalle_pedidos (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER NOT NULL REFERENCES pedidos(id) ON DELETE CASCADE,
    producto_id INTEGER NOT NULL REFERENCES productos(id),
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unitario DECIMAL(10, 2) NOT NULL
);