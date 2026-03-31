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



PARTE 2
Replique las tablas creadas anteriormente en 
🔗 Ejercicio de Bases de Datos, con sus respectivos PKs, FKs
.constraints, y demás requerimientos.

Investigue cómo hacer que los PKs se generen automáticamente.
Utilice los tipos de datos adecuados.
Si existe alguna limitante por SQLite, documéntela y
resuelva la limitante como considere adecuado.

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

--5. Obtenga todas las facturas realizadas po el mismo comprador

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



