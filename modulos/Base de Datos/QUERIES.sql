-- SQLite.
PARTE 1
Cree una nueva base de datos en SQLite.

--Tabla Productos

-- CREATE TABLE Productos (
        -- ID INTEGER PRIMARY KEY,
        -- Tipo TEXT NOT NULL,
        -- Precio REAL NOT NULL,
        -- Fecha TEXT NOT NULL
        -- );

--Tabla Facturas
-- CREATE TABLE Facturas (
        -- ID INTEGER PRIMARY KEY,      
        -- Fecha TEXT NOT NULL,
        +--EMAIL TEXT NOT NULL UNIQUE,
        -- Total REAL NOT NULL
        -- );

--Tabla Detalles_Factura
-- CREATE TABLE Detalles_Factura (
        -- ID_DETALLE INTEGER PRIMARY KEY,
        -- ID_FACTURA INTEGER REFERENCES Facturas(ID),
        -- ID_PRODUCTO INTEGER REFERENCES Productos(ID),
        -- Cantidad INTEGER NOT NULL
        -- );

--Tabla Carrito_Compras
    -- CREATE TABLE Carrito_Compras (
        -- ID INTEGER PRIMARY KEY,
        -- ID_USUARIO INTEGER REFERENCES Facturas(EMAIL),
        -- Fecha TEXT NOT NULL
        -- );

--Tabla Carrito_Productos
    -- CREATE TABLE Carrito_Productos (Y,
        -- ID_CARRITO INTEGER REFERENCES Carrito_Compras(ID),
        -- ID_PRODUCTO INTEGER REFERENCES Productos(ID),
        -- Cantidad INTEGER NOT NULL
        -- );
--PARTE 2
--Replique las tablas creadas anteriormente en 
--🔗 Ejercicio de Bases de Datos, con sus respectivos PKs, FKs
--constraints, y demás requerimientos.

--insertando datos de prueba

--INSERT INTO Productos (id,Tipo, Precio, Fecha)
--VALUES (1111, 'Coffe-Maker', 10000, '2024-01-01');
--INSERT INTO  Productos (id,Tipo, Precio, Fecha)
--VALUES (2222, 'Olla-Arrocera', 25000, '2024-01-02');
--INSERT INTO Productos (id,Tipo, Precio, Fecha)
--VALUES (3333, 'Cocina', 223000, '2024-01-03');   
--INSERT INTO Productos (id,Tipo, Precio, Fecha)
--VALUES (4444, 'Lavadora', 198500, '2024-03-01');      
--INSERT INTO Productos (id,Tipo, Precio, Fecha)
--VALUES (5555, 'Microondas', 45000, '2024-01-05');    


--INSERT INTO Facturas (ID, Fecha, EMAIL, Total, Numero_Telefono, Codigo_Empleado)
--VALUES (1, '2024-01-10', 'cliente1@example.com', 10000, '123456789', 'EMP001');

--INSERT INTO Facturas (ID, Fecha, EMAIL, Total, Numero_Telefono, Codigo_Empleado)
--VALUES (2, '2024-01-11', 'cliente2@example.com', 25000, '987654321', 'EMP002');

--INSERT INTO Facturas (ID, Fecha, EMAIL, Total, Numero_Telefono, Codigo_Empleado)
--VALUES (3, '2024-01-12', 'cliente3@example.com', 223000, '555555555', 'EMP003');

--INSERT INTO Facturas (ID, Fecha, EMAIL, Total, Numero_Telefono, Codigo_Empleado)
--VALUES (4, '2024-03-01', 'cliente4@example.com', 198500, '111111111', 'EMP004');

--INSERT INTO Detalles_Factura (ID_DETALLE, ID_FACTURA, ID_PRODUCTO, Cantidad)
--VALUES (1, 1, 1111, 1);
--INSERT INTO Detalles_Factura (ID_DETALLE, ID_FACTURA, ID_PRODUCTO, Cantidad)
--VALUES (2, 2, 2222, 1);
--INSERT INTO Detalles_Factura (ID_DETALLE, ID_FACTURA, ID_PRODUCTO, Cantidad)
--VALUES (3, 3, 3333, 1);
--INSERT INTO Detalles_Factura (ID_DETALLE, ID_FACTURA, ID_PRODUCTO, Cantidad)
--VALUES (4, 4, 4444, 1);

--INSERT INTO Carrito_Compras (ID, ID_USUARIO, Fecha)
--VALUES (1, 'cliente1@example.com', '2024-01-10');
--INSERT INTO Carrito_Compras (ID, ID_USUARIO, Fecha)
--VALUES (2, 'cliente2@example.com', '2024-01-11');
--INSERT INTO Carrito_Compras (ID, ID_USUARIO, Fecha)
--VALUES (3, 'cliente3@example.com', '2024-01-12');
--INSERT INTO Carrito_Compras (ID, ID_USUARIO, Fecha)
--VALUES (4, 'cliente4@example.com', '2024-01-13');

--INSERT INTO Carrito_Productos (ID_CARRITO, ID_PRODUCTO, Cantidad)
--VALUES (1, 1111, 1);
--INSERT INTO Carrito_Productos (ID_CARRITO, ID_PRODUCTO, Cantidad)
--VALUES (2, 2222, 1);
--INSERT INTO Carrito_Productos (ID_CARRITO, ID_PRODUCTO, Cantidad
--VALUES (3, 3333, 1);
--INSERT INTO Carrito_Productos (ID_CARRITO, ID_PRODUCTO, Cantidad
--VALUES (4, 4444, 1);


--Investigue cómo hacer que los PKs se generen automáticamente.
--Utilice los tipos de datos adecuados.
--Si existe alguna limitante por SQLite, documéntela y
--resuelva la limitante como considere adecuado.

Investigacion:

Como se genera los PK'S automaticamente en SQLite?
El commando INTEGER PRIMARY KEY: se convierte en rowed y genera automaticamente un valor unico.
AUTOINCREMENT: hace que los ID'S no se reutilicen, aunque el registro sea borrado
la limitante va en que puede causar fragmentacion y crecimiento innecesario.

Tipos de Datos 
ID'S y cantidades: INTEGER
Precios y Totales: REAL
FECHAS: TEXT (YYY-MM-DD HH:MM:SS)
EMAILS Y NOMBRES : TEXT, NOT NULL Y UNIQUE

Limitaciones: no existe DATE O DATE TIME, solo text en Formato ISO 
REAL puede aceptar texto.
Es mas eficiente INTEGER PRIMARY KEY QUE AUTOINCREMENT.

PARTE 3
Utilizando el comando ALTER,
modifique la tabla de Facturas y
agregue una columna para almacenar también el número de teléfono del comprador,
y otra para el código de empleado del cajero que realizó la venta.

--TABLA FACTURAS
--ALTER TABLE Facturas
--ADD NUEMRO_TELEFONO TEXT;

--ALTER TABLE Facturas
--ADD CODIGO_EMPLEADO TEXT; 

--ACTULIZAR LOS REGISTROS EXISTENTES

--UPDATE Facturas SET\--NUMERO_TELEFONO = '24545678',
--CODIGO_EMPLEADO = 2
--WHERE ID = 1;    

--UPDATE Facturas SET
--NUMERO_TELEFONO = '24545679',
--CODIGO_EMPLEADO = 1
--WHERE ID = 2;

--UPDATE Facturas SET
--NUMERO_TELEFONO = '24545680',
--CODIGO_EMPLEADO = 3
--WHERE ID = 3;

--UPDATE Facturas SET
--NUMERO_TELEFONO = '24545681',
--CODIGO_EMPLEADO = 1
--WHERE ID = 4;


PARTE 4
--1. Obtenga todos los productos almacenados

--SELECT Tipo
--FROM Productos;

--2. Obtenga todos los productos que tengan un precio mayor a 50000

-- SELECT Tipo
-- FROM Productos
-- WHERE Precio > 50000:

--3. Obtenga todas las compras de un producto por id
--SELECT *
--FROM Detalles_Factura
--WHERE ID_PRODUCTO = 1;    


--4. Obtenga todas las compras agrupadas por producto, donde se muestre el total
--comprado entre todas las facturas.

--SELECT ID_PRODUCTO,
--SUM(Cantidad) AS Total_Comprado
--FROM Detalles_Factura
--GROUP BY ID_PRODUCTO;     

--5. Obtenga todas las facturas realizadas por el mismo comprador

--SELECT EMAIL, 
--COUNT(*) AS Total_Facturas
--FROM Facturas;

--6. Obtenga todas las facturas ordenas por monto total de forma descendente

--SELECT *
--FROM Facturas
--ORDER BY Total DESC;

--7. Obtenga una sola factura por numero de factura

--SELECT *
--FROM Facturas
--WHERE ID = 1; 

--cambios solicitados

-- mismo formato 

--cambio de nombre de columna Facturas

--ALTER TABLE Facturas
--RENAME COLUMN id to Id;
--ALTER TABLE Facturas
--RENAME COLUMN EMAIL to Email;
--ALTER TABLE Facturas
--RENAME COLUMN Numero_telefono to Numero_Telefono;
--ALTER TABLE Facturas
--RENAME COLUMN Codigo_empleado to Codigo_Empleado;

--cambio de nombre de columna Detalle_Factura

--ALTER TABLE Detalles_Factura
--RENAME COLUMN ID_DETALLE to Id_Detalle;

--ALTER TABLE Detalles_Factura
--RENAME COLUMN ID_FACTURA to Factura_Id;

--ALTER TABLE Detalles_Factura
--RENAME COLUMN ID_PRODUCTO to Id_Producto;

--ALTER TABLE Detalles_Factura
--RENAME COLUMN Cantidad to Cantidad;   

--ALTER TABLE Detalles_Factura
--RENAME COLUMN Id_Producto to Producto_Id;

--Cambio de nombre de columna Carrito_Productos

--ALTER TABLE Carrito_Productos
--RENAME COLUMN id to Id;

--ALTER TABLE Carrito_Productos
--RENAME COLUMN id_producto to Producto_Id;

--ALTER TABLE Carrito_Productos
--RENAME COLUMN cantidad to Cantidad;

--Cambio de nombre de columna Carrito_Compras

--ALTER TABLE Carrito_Compras
--RENAME COLUMN id to Id;

--ALTER TABLE Carrito_Compras
--RENAME COLUMN id_Usuario to Usuario_Id;

--Cambio de nombre de columna Productos

--ALTER TABLE Productos
--RENAME COLUMN id to Id;

--Cambios en parte 4 pregunta 5
--Obtenga todas las facturas realizadas por el mismo comprador


--SELECT *
--FROM Facturas
--WHERE EMAIL = 'cliente2@example.com';




