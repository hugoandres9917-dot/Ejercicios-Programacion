--Ejercicio 1: Creación de la base de datos
--Plantee una base de datos simple que incluya las siguientes entidades:
--Products
--Users
--Bills

--ejercicio1_creacion.sql

DO $$
BEGIN
    -- reiniciar el ejerecicio eliminar tablas si existen
    DROP TABLE IF EXISTS Bill_Details;
    DROP TABLE IF EXISTS Bills;
    DROP TABLE IF EXISTS Products;
    DROP TABLE IF EXISTS Users;

    -- Tabla de Usuarios
    CREATE TABLE Users (
        user_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(150) UNIQUE NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

    --Tabla de Productos
    CREATE TABLE Products (
        product_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price NUMERIC(10,2) NOT NULL,
        stock INT NOT NULL CHECK (stock >= 0)
        );

    --Tabla de Facturas
    CREATE TABLE Bills (
        bill_id SERIAL PRIMARY KEY,
        user_id INT NOT NULL REFERENCES Users(user_id),
        bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total NUMERIC(10,2) NOT NULL DEFAULT 0
        );

    --Tabla cruz: detalle de factura
    CREATE TABLE Bill_Details (
        detail_id SERIAL PRIMARY KEY,
        bill_id INT NOT NULL REFERENCES Bills(bill_id) On DELETE CASCADE,
        product_id INT NOT NULL REFERENCES Products(product_id),
        quantity INT NOT NULL CHECK (quantity > 0),
        subtotal NUMERIC(12,2) NOT NULL
        );

    RAISE NOTICE 'Base de datos creada con exito: Users, Products, Bills, Bill_Details';
END;
$$;

