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



--cambios solicitados
--Para la Tabla Automovimoviles, la forma que hemos averiguado para eleiminar
--los siguientes problemas
-- make y model dependen entre si no por su VIN- rompe 3FN
--owner_name y owner_Phone dependen de owner_ID no de VIN-REDUNDANCIA
--InsuranceCompany no depende de poliza si no poliza depende de compañia- rompe 2FN
--una poliza puede cubrir varios vehiculos-- creamos tabla puente entre policy-vehicle

---Nuevo esquema de tablas

--tabla Make
--tabla Model
--tabla Automoviles
--Tabla Owner
--tabla Company
--tabla Policy
--tabla Policy_Vehicle


CREATE TABLE Make (
  ID INTEGER PRIMARY KEY,
  MakeName TEXT NOT NULL
);

CREATE TABLE Model (
    ID INTEGER PRIMARY KEY,
    Make_Id INTEGER REFERENCES Make(ID),
    Model_Name TEXT NOT NULL
);

CREATE TABLE Automoviles (
  VIN TEXT PRIMARY KEY,
  Model_Id INTEGER REFERENCES Model(ID),
  Year INTEGER NOT NULL,
  Color TEXT NOT NULL
);
CREATE TABLE Owners (
  Owner_ID INTEGER PRIMARY KEY,
  Owner_Name TEXT NOT NULL,
  Owner_Phone TEXT NOT NULL
);

CREATE TABLE Company (
  ID INTEGER PRIMARY KEY,
  Company_Name TEXT NOT NULL
);

CREATE TABLE Policy (
  ID INTEGER PRIMARY KEY,
  Policy_Number TEXT NOT NULL,
  Coverage_Type TEXT NOT NULL, -- EJEMPLO COVERTURA TOTAL
  Company_Id INTEGER REFERENCES Company(ID)
);

CREATE TABLE Owner_Policy (
    Owner_ID INTEGER REFERENCES Owners(Owner_ID),
    Policy_Id integer REFERENCES Policy(ID)
);


CREATE TABLE Policy_Vehicle (
  PolicyID INTEGER NOT NULL,
  VIN TEXT NOT NULL,
  Owner_ID INTERGER REFERENCES Owners(Owner_Id),
  PRIMARY KEY (PolicyID, VIN),
  FOREIGN KEY (PolicyID) REFERENCES Policy(ID),
  FOREIGN KEY (VIN) REFERENCES Automoviles(VIN)
);

---Insertamos los datos en las nuevas tablas 

--Tabla Make
INSERT INTO Make (ID, MakeName)
VALUES (1, 'Honda');
INSERT INTO Make (ID, MakeName)
VALUES(2, 'Chevrolet');

--Tabla Model
INSERT INTO Model (ID, Model_Name, Make_Id)
VALUES (1, 'Accord', 1);
INSERT INTO Model (ID, Model_Name, Make_Id)
VALUES (2, 'CR-V', 1);
INSERT INTO Model (ID, Model_Name,Make_Id)
VALUES (3, 'Volt', 2);

--Tabla Automoviles
INSERT INTO Automoviles (VIN, Model_Id, Year, Color)
VALUES ('1HGCM82633A', 1, 2003, 'Silver');
INSERT INTO Automoviles (VIN, Model_Id, Year, Color)
VALUES ('5J6RM4H79EL', 2, 2014, 'Blue');
INSERT INTO Automoviles (VIN, Model_Id, Year, Color)
VALUES ('1G1RA6EH1FU', 3, 2015, 'Red');

--Tabla Owner
INSERT INTO Owners (Owner_ID, Owner_Name, Owner_Phone)
VALUES (101, 'Alice', '123-456-7890');
INSERT INTO Owners (Owner_ID, Owner_Name, Owner_Phone)
VALUES (102,'Bob', '987-654-3210');
INSERT INTO Owners (Owner_ID, Owner_Name, Owner_Phone)
VALUES (103, 'Claire', '555-123-4567');
INSERT INTO Owners (Owner_ID, Owner_Name, Owner_Phone)
VALUES (104, 'Dave', '111-222-3333');


--Tabla Compay (Seguros)

INSERT INTO Company (ID, Company_Name)
VALUES (1, 'ABC Insurance');
INSERT INTO Company (ID, Company_Name)
VALUES (2, 'XYZ Insurance');
INSERT INTO Company(ID, Company_Name)
VALUES (3, 'DEF Insurance');
INSERT INTO Company (ID, Company_Name)
VALUES (4, 'GHI Insurance');


--Tabla Policy
INSERT INTO Policy(ID, Policy_Number, Coverage_type, Company_Id)
VALUES (1, 'POL12345','Cobertura Total', 1);
INSERT INTO Policy (ID, Policy_Number, Coverage_type, Company_Id)
VALUES (2, 'POL54321', 'Cobertura de accidente deducible', 2);
INSERT INTO Policy (ID, Policy_Number, Coverage_type, Company_Id)
VALUES (3, 'POL67890', 'Cobertura a terceros', 3);
INSERT INTO Policy (ID, Policy_Number, Coverage_type, Company_Id)
VALUES (4, 'POL98765', 'Cobertura asistencia en camino', 4);


--TABLA Owner_Policy
INSERT INTO Owner_Policy (Owner_ID, Policy_Id)
VALUES (101, 1);
INSERT INTO Owner_Policy (Owner_ID, Policy_Id)
VALUES (102, 2);
INSERT INTO Owner_Policy (Owner_ID, Policy_Id)
VALUES (103, 3);
INSERT INTO Owner_Policy (Owner_ID, Policy_Id)
VALUES (104, 4);
INSERT INTO Owner_Policy (Owner_ID, Policy_Id)
VALUES (101, 3); 

--Tabla Policy_Vehicle

INSERT INTO Policy_Vehicle (PolicyID, VIN, Owner_ID)
VALUES (1, '1HGCM82633A', 101);
INSERT INTO Policy_Vehicle (PolicyID, VIN, Owner_ID)
VALUES (2, '1HGCM82633A', 102);
INSERT INTO Policy_Vehicle (PolicyID, VIN, Owner_ID)
VALUES (3, '5J6RM4H79EL', 103);
INSERT INTO Policy_Vehicle (PolicyID, VIN, Owner_ID)
VALUES (4, '1G1RA6EH1FU', 104);
INSERT INTO Policy_Vehicle (PolicyID, VIN, Owner_ID)
VALUES (3, '1HGCM82633A', 101);




DROP TABLE Owner_Policy

--Comprendo ahora la opcion que mesionas seria mover Owner_ID 
--para la tabla cruz Policy vehicle ya existente para asi eliminar 
--la creacion de mas tablas , esto permite que la poliza se siga aplicando 
--a mas vahiculos y
--que varios duenos contraten la misma poliza, esta manera es mas agil creo