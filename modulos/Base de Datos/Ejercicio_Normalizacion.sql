-- SQLite

--Normalice las siguiente tablas:
--Asegurese de incluir en la solución todos los pasos y justificaciones sobre la normalización. También incluya todas las tablas intermedias por las que fue pasando antes de llegar a la solución final.
--
-- Normalizacion de la base de datos
-- Creacion de tablas

--CREATE TABLE Ordenes (
    --Order_ID INTEGER NOT NULL,
    --Customer_Name VARCHAR(255) NOT NULL,
    --Customer_Phone TEXT NOT NULL,
    --Address VARCHAR(255) NULL,
    --Item_Id INTEGER NOT NULL,
    --Item_Name TEXT NOT NULL,
    --Price REAL NOT NULL,
    --Quantity INTEGER NOT NULL,
    --Special_Requests TEXT,
    --Delivery_time TEXT NOT NULL
--);

--Insertamos los datos de la tabla Ordenes 

--INSERT INTO Ordenes(Order_ID, Customer_Name, Customer_Phone, Address, Item_Id, Item_Name, Price, Quantity, Special_Requests, Delivery_Time)
--VALUES (001, 'Alice', '123-456-7890', '123 Main St', 101, 'Cheeseburger', 8.00, 1, 'Extra cheese', '6:00 PM');

--INSERT INTO Ordenes (Order_ID, Customer_Name, Customer_Phone, Address, Item_Id, Item_Name, Price, Quantity, Special_Requests, Delivery_Time)
--VALUES ('001', 'Alice', '123-456-7890', '123 Main St', 102, 'Fries', 3.00, 1, 'Extra Ketchup', '6:00 PM');

--INSERT INTO Ordenes (Order_ID, Customer_Name, Customer_Phone, Address, Item_Id, Item_Name, Price, Quantity, Special_Requests, Delivery_Time)
--VALUES ('002', 'Bob', '987-654-3210', '456 Elm St', 104, 'Fries', 3.00, 1, 'NONE', '7:30 PM');

--INSERT INTO Ordenes (Order_ID, Customer_Name, Customer_Phone, Address, Item_Id, Item_Name, Price, Quantity, Special_Requests, Delivery_Time)
--VALUES ('003', 'CLAIRE', '555-123-4567', '789 Oak St', 105, 'Salad', 6.00, 1, 'No croutons', '12:00 PM');

--INSERT INTO Ordenes (Order_ID, Customer_Name, Customer_Phone, Address, Item_Id, Item_Name, Price, Quantity, Special_Requests, Delivery_Time)
--VALUES ('004', 'CLAIRE', '555-123-4567','464 Georgia st', 106, 'Water', 1.00, 1, 'None', '1:00 PM');

--INSERT INTO Ordenes (Order_ID, Customer_Name, Customer_Phone, Address, Item_Id, Item_Name, Price, Quantity, Special_Requests, Delivery_Time)
--VALUES ('002', 'Bob', '987-654-3210', '456 elm St', 103, 'Pizza', 12.00, 1, 'Extra cheese', '7:30 PM');

--Problemas de la tabla Ordenes
--1. Redundancia: datos del cliente  y direccion repetridos

--2. Dependencia parcial: el precio depende del producto, no del pedido

--3. Posibles inconsistencias: Claire aparace con dos direcciones distintas

--Normalizacion de la base de datos

-- La tabla ya en parte cumple con 1FN,si, listas ni atibutos multivaluados ya cumple con 1FN, pero hay redundancia. 
--- los atributos deben depender de la PK, opciones: (1.OrdeID, Item_Id).

--Customer_name, phone y address dependen solo de Order_ID.ABORT
--Price depende solo de Item_Id.

--separamos en tablas:
--
--Tabla Customer: Customer_ID, Customer_Name, Customer_Phone

--Tabla Addresses: Address_Id, Customer_Id, Address

--Tabla Items: Item_Id, Item_Name, Price

--Tabla Orders: Order_ID, Customer_Id, DeliveryTime

--Tabla OrderDetails: Order_ID, Item_Id, Quatity, SpecialRequests

-- con este diseño, cada tabla tiene una clave primaria y los atributos
-- dependen completamente de la clave primaria, eliminando la redundancia
--y las posibles inconsistencias.

--en customers, el telefono depende directamente del cliente.
--en addresses, la direccion depende de Address_Id
--en Items, el precio depende del producto
--en Orders, DeliveryTime depende del pedido
--en OrderDetails, Quantity y SpecialRequests dependen de la
--combinacion de Order_ID y Item_Id


--Creamos las tablas normalizadas

--CREATE TABLE Customers (
--    Customer_ID INTEGER PRIMARY KEY,
--    Customer_Name VARCHAR(255) NOT NULL,
--    Customer_Phone TEXT NOT NULL
--);

--CREATE TABLE Addresses (
--    Address_ID INTEGER PRIMARY KEY,
--    Customer_ID INTEGER REFERENCES Customers(Customer_ID),
--    Address VARCHAR(255) NOT NULL
--);

--CREATE TABLE Items (
--    Item_ID INTEGER PRIMARY KEY,
--    Item_Name TEXT NOT NULL,
--    Price REAL NOT NULL
--);

--CREATE TABLE Orders (
--    Order_ID INTEGER PRIMARY KEY,
--    Customer_ID INTEGER REFERENCES Customers(Customer_ID),
--    Delivery_Time TEXT NOT NULL
--);

----CREATE TABLE OrderDetails (
--    Order_ID INTEGER REFERENCES Orders(Order_ID),
--    Item_ID INTEGER REFERENCES items(Item_ID),
--    Quantity INTEGER NOT NULL,
--    Special_Requests TEXT
--);

---Insertamos datos en las tablas
--TABLA Customers
--INSERT INTO Customers (Customer_ID, Customer_Name,Customer_Phone)
--VALUES (1, 'Alice', '123-456-7890');

--INSERT INTO Customers (Customer_ID, Customer_Name,Customer_Phone)
--VALUES (2, 'Bob', '987-654-3210');

--INSERT INTO Customers (Customer_ID, Customer_Name,Customer_Phone)
--VALUES (3, 'Claire', '555-123-4567');

--TABLA Addresses

--INSERT INTO Addresses (Address_ID, Customer_ID, Address)
--VALUES (1, 1, '123 MAIN ST');

--INSERT INTO Addresses (Address_ID, Customer_ID, Address)
--VALUES (2, 2, '456 ELM ST');

--INSERT INTO Addresses (Address_ID, Customer_ID, Address)
--VALUES (3, 3, '780 OAK ST');

--INSERT INTO Addresses (Address_ID, Customer_ID, Address)
--VALUES (4, 3, '464 GEORGIA ST');


--TABLA Items

--INSERT INTO Items (Item_ID, Item_Name, Price)
--VALUES (101, 'cheeseburger', 8.0);

--INSERT INTO Items (Item_ID, Item_Name, Price)
--VALUES (102, 'fries', 3.0);

--INSERT INTO Items (Item_ID, Item_Name, Price)
--VALUES ( 103, 'Pizza', 12.0);

--INSERT INTO Items ( Item_ID, Item_Name, Price)
--VALUES (104, 'Salad', 6.0);

--INSERT INTO Items (Item_ID, Item_Name, Price)
--VALUES (105, 'Water', 1.0);

--TABLA Orders

--INSERT INTO Orders (Order_ID, Customer_ID, Delivery_Time)
--VALUES (1, 'Alice', '6:00 pm');

--INSERT INTO Orders (Order_ID, Customer_ID, Delivery_Time)
--VALUES (2, 'Bob', '7:30 pm');


--INSERT INTO Orders (Order_ID, Customer_ID, Delivery_Time)
--VALUES (3, 'Claire', '12:00 pm');

--INSERT INTO Orders (Order_ID, Customer_ID, Delivery_Time)
--VALUES (4, 'Claire', '1:00 pm');

--TABLA OrderDetails

--INSERT INTO OrderDetails (Order_ID, Item_ID, Quantity, Special_Requests)
--VALUES (1, 101, 1, 'Extra Cheese');

--INSERT INTO OrderDetails (Order_ID, Item_ID, Quantity, Special_Requests)
--VALUES (1, 102, 1, 'Extra Ketchup');

--INSERT INTO OrderDetails ( Order_ID, Item_ID, Quantity, Special_Requests)
--VALUES (2, 102, 1,'None');

--INSERT INTO OrderDetails (Order_ID, Item_ID, Quantity, Special_Requests)
--VALUES (2, 103, 1, 'Extra Cheese');

--INSERT INTO OrderDetails ( Order_ID, Item_ID, Quantity, Special_Requests)
--VALUES (3, 104, 1, 'No Croutons');

--INSERT INTO OrderDetails (Order_ID, Item_ID, Quantity, Special_Requests)
--VALUES (4, 105, 1, 'None');



---Normalizacion TABLA Automoviles

--creamos la tabla original y insertamos sus datos.Address

--CREATE TABLE Automoviles(
    --VIN TEXT NOT NULL,
    --Make TEXT NOT NULL,
    --Model TEXT NOT NULL,
    --Year INTEGER NOT NULL,
    --Color TEXT NOT NULL,
    --Owner_ID INTEGER NOT NULL,
    --Owner_Name TEXT NOT NULL,
    --Owner_Phone TEXT NOT NULL,
    --InsuranceCompany TEXT NOT NULL,
    --InsurancePolicy TEXT NOT NULL
);

--INSERTAMOS LOS DATOS
--INSERT INTO Automoviles (VIN, Make, Model, Year, Color, OwnerID, OwnerName, OwnerPhone, InsuranceCompany, InsurancePolicy)
--VALUES ('1HGCM82633A','Honda','Accord',2003,'Silver',101,'Alice','123-456-7890','ABC Insurance','POL12345');

--INSERT INTO Automoviles (VIN, Make, Model, Year, Color, OwnerID, OwnerName, OwnerPhone, InsuranceCompany, InsurancePolicy)
--VALUES ('1HGCM82633A','Honda','Accord',2003,'Silver',102,'Bob','987-654-3210','XYZ Insurance','POL54321');

--INSERT INTO Automoviles (VIN, Make, Model, Year, Color, OwnerID, OwnerName, OwnerPhone, InsuranceCompany, InsurancePolicy)
--VALUES ('5J6RM4H79EL','Honda','CR-V',2014,'Blue',103,'Claire','555-123-4567','DEF Insurance','POL67890');

--INSERT INTO Automoviles (VIN, Make, Model, Year, Color, OwnerID, OwnerName, OwnerPhone, InsuranceCompany, InsurancePolicy)
--VALUES ('1G1RA6EH1FU','Chevrolet','Volt',2015,'Red',104,'Dave','111-222-3333','GHI Insurance','POL98765');

--Problemas
--El mismo VIN puede tener varios dueños
--Datos del dueño y de la poliza se repiten
--hay dependencias, el seguro depende del dueño, no del automovil.Address
--exite redundancia

--separar entidades

--Automoviles(VIN, Make, Model, Year, Color)
--Owners (Owner_ID, Owner_Name, Owner_Phone)
--Insurance(Policy_ID, Company, PolicyNumber, Owner_ID)
--Ownership (VIN, Owner_ID) TABLA CRUZ RELACION N;N

--Eliminamos dependencias transitivas:
--El seguro depende del dueño
--El automovil depende solo del VIN
--El dueño depende solo de Owner_ID

--Creando Tablas Normalizadas

--Tabla Automoviles

--CREATE TABLE Automoviles1 (
  --VIN TEXT PRIMARY KEY,
  --Make TEXT NOT NULL,
  --Model TEXT NOT NULL,
  --Year INTEGER NOT NULL,
  --Color TEXT NOT NULL
);

--TABLA DUEñOS

--CREATE TABLE Owners (
  --Owner_ID INTEGER PRIMARY KEY,
  --Owner_Name TEXT NOT NULL
  --Owner_Phone TEXT NOT NULL
--);

--TABLA SEGUROS

--CREATE TABLE Insurance (
    --Policy_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    --Company TEXT NOT NULL,
    --PolicyNumber TEXT NOT NULL,
    --Owner_ID INTEGER REFERENCES Owners(Owner_ID)
--);

-- TABLA CRUZ
--CREATE TABLE Ownership (
    --VIN TEXT REFERENCES Automoviles1(VIN),
    --Owner_ID INTEGER REFERENCES Owners(Owner_ID)
--);
    


--Insertamos los datos en las tablas

--Automoviles

--INSERT INTO Automoviles1 (VIN, Make, Model, Year, Color)
--VALUES ('1HGCM82633A', 'Honda', 'Accord', 2003, 'silver');
--INSERT INTO Automoviles1 (VIN, Make, Model, Year, Color)
--VALUES ('5J6RM4H79EL', 'Honda', 'CR-V', 2014, 'Blue');
--INSERT INTO Automoviles1 (VIN, Make, Model, Year, Color)
--VALUES ('1G1RA6EH1FU', 'Chevrolet', 'Volt', 2015, 'Red');

--Dueños

--INSERT INTO Owners(Owner_ID, Owner_Name, Owner_Phone)
--VALUES (101, 'Alice', '123-456-7890');
--INSERT INTO Owners(Owner_ID, Owner_Name, Owner_Phone)
--VALUES (102, 'Bob', '987-654-3210');
--INSERT INTO Owners(Owner_ID, Owner_Name, Owner_Phone)
--VALUES (103, 'Claire', '555-123-4567');
--INSERT INTO Owners(Owner_ID, Owner_Name, Owner_Phone)
--VALUES (104, 'Dave', '111-222-3333');


--Seguros

--INSERT INTO Insurance (Policy_ID, Company, PolicyNumber, Owner_ID)
--VALUES (1, 'ABC Insurance', 'POL12345', 101);
--INSERT INTO Insurance (Policy_ID, Company, PolicyNumber, Owner_ID)
--VALUES (2, 'XYZ Insurance', 'POL54321', 102);
--INSERT INTO Insurance (Policy_ID, Company, PolicyNumber, Owner_ID)
--VALUES (3, 'DEF Insurance', 'POL67890', 103);
--INSERT INTO Insurance (Policy_ID, Company, PolicyNumber, Owner_ID)
--VALUES (4, 'GHI Insurance', 'POL98765', 104);

-- TABLA CRUZ Ownership

--INSERT INTO Ownership (VIN, Owner_ID)
--VALUES ('1HGCM82633A', 101);
--INSERT INTO Ownership (VIN, Owner_ID)
--VALUES ('1HGCM82633A', 102);
--INSERT INTO Ownership (VIN, Owner_ID)
--VALUES ('5J6RM4H79EL', 103);
--INSERT INTO Ownership (VIN, Owner_ID)
--VALUES ('1G1RA6EH1FU', 104);

--Con este diseño de tablas podemos cargar datos sin duplicarlos y manejar casos de multiples dueños 








