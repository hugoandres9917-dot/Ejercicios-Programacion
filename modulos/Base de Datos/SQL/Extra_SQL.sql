-- SQLite
--Crear categorías y ajustar productos
--Cree la tabla categories con:
--id (PK autoincrement)
--name (UNIQUE, NOT NULL)
--description

    --CREATE TABLE Categories (
        --id INTEGER PRIMARY KEY AUTOINCREMENT,
        --name TEXT UNIQUE NOT NULL,
        --description TEXT
    --);

--Agregue a products la columna category_id (INTEGER, puede permitir NULL)

        --ALTER TABLE Productos
        --ADD COLUMN Category_Id INTEGER;


--Inserte al menos 3 filas en categories

        --INSERT INTO Categories (Id, Nombre, descripcion)
        --VALUES (1, 'Ropa', 'Ropa y accesorios');

        --INSERT INTO Categories (Id, Nombre, descripcion)
        --VALUES (2, 'Electronica', 'Dispositivos electronicos');
    
        --INSERT INTO Categories (Id, Nombre, descripcion)
        --VALUES (3, 'Hogar', 'Muebles y decoracion');


--Actualice algunos products asignándoles un category_id

        --UPDATE Productos SET
        --Category_Id = 1
        --WHERE Tipo IN ('Coffe-Maker', 'Olla-Arrocera', 'Microondas');

        --UPDATE Productos SET
        --Category_Id = 2
        --WHERE Tipo IN ('Cocina');

        --UPDATE Productos SET
        --Category_Id = 3
        --WHERE Tipo IN ('Lavadora');


--Verifique con SELECT * FROM products
----(muestre id, product_name, price, category_id, stock_available).

        --SELECT * FROM Productos;

--2. Carga de productos y filtros básicos
--Inserte al menos 10 filas en products con product_name, price, stock_available

--AGREGAMOS COLUMNA Disponible_stock

        --ALTER TABLE Productos
        --ADD COLUMN Disponible_stock INTEGER DEFAULT 0;

--INSERTANDO MAS productos 

        --INSERT INTO Productos (id,Tipo, Precio, Fecha,Category_Id, Disponible_stock)
        --VALUES (6666, 'Sillones', 600000, '2023-01-06', 3, 5),

        --INSERT INTO Productos (id,Tipo, Precio, Fecha,Category_Id, Disponible_stock)
        --VALUES ('Television', 700000, '2023-01-07', 2, 10),
        
        --INSERT INTO Productos (id,Tipo, Precio, Fecha,Category_Id, Disponible_stock)
        --VALUES (8, 'Mesa_comedor', 800000, '2023-01-08', 3, 15),
        
        --INSERT INTO Productos (id,Tipo, Precio, Fecha,Category_Id, Disponible_stock)
        --VALUES (9, 'Tostador', 900000, '2023-01-09', 2, 20),


        --INSERT INTO Productos (id,Tipo, Precio, Fecha,Category_Id, Disponible_stock)
        --VALUES (10, 'Cortinas', 1000000, '2023-01-10', 1, 25);



        --UPDATE Productos SET
            --Id=1, Tipo='Coffe-Maker', Precio=10000, Fecha='2024-01-15', Category_Id=1, Disponible_stock=10
        --WHERE Id=1111;

        --UPDATE Productos SET
            --Id=2, Tipo='Olla-Arrocera', Precio=5000, Fecha='2024-02-20', Category_Id=1, Disponible_stock=15
        --WHERE Id=2222;

        --UPDATE Productos SET
            --Id=3, Tipo='Microondas', Precio=15000, Fecha='2024-03-10', Category_Id=1, Disponible_stock=8
        --WHERE Id=3333;          

        --UPDATE Productos SET
            --Id=4, Tipo='Cocina', Precio=20000, Fecha='2024-04-05', Category_Id=2, Disponible_stock=5
        --WHERE Id=4444;

        --UPDATE Productos SET
            --Id=5, Tipo='Lavadora', Precio=25000, Fecha='2024-05-01', Category_Id=2, Disponible_stock=3
        --WHERE Id=5555;      

        --UPDATE Productos SET
            --Id=6, Tipo='Sofa', Precio=30000, Fecha='2024-06-01', Category_Id=3, Disponible_stock=2
        --WHERE Id=6666;  

--Seleccione todos los productos

        --SELECT*
        --FROM Productos;

--Seleccione productos con price > 5００００

        --SELECT *
        --FROM Productos
        --WHERE Precio > 50000; 


--Seleccione productos cuyo product_name contenga la palabra “apple” usando LIKE

        --SELECT *
        --FROM Productos
        --WHERE Tipo LIKE '%Sofa%';


--Liste los 5 productos más caros con ORDER BY price DESC LIMIT 5

        --SELECT *
        --FROM Productos
        --ORDER BY Precio DESC
        --LIMIT 5;

--3.Correcciones de datos en productos
--Establezca stock_available = 0 donde price <= 0

        --UPDATE Productos
        --SET Disponible_stock = 0
        --WHERE Precio <= 0;
        
--Aumente el price en 100 unidades para todos los productos cuando stock_available sea menor a 10

        --UPDATE Productos
        --SET Precio = Precio + 100
        --WHERE Disponible_stock < 10;

--Disminuya stock_available en 1 para un product_id específico
        
        --UPDATE Productos
        --SET Disponible_stock = Disponible_stock - 1
        --WHERE Id = 1;

--Verifique con SELECT * FROM products ORDER BY id ASC LIMIT 10
        
        --SELECT *
        --FROM Productos
        --ORDER BY Id ASC
        --LIMIT 10;