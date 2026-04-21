-- EJERCICIO JOINs

--Cree las tablas en una base de datos SQL y realice las siguientes operaciones:
--Debe entregar todos los queries realizados y capturas del resultado.
--2. Para los siguientes ejercicios, utilice las siguientes tablas:

--creamos las tablas
CREATE TABLE Books (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Author INTEGER REFERENCES Authors(ID)
);

CREATE TABLE Authors (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(100) NOT NULL
);


CREATE TABLE Authors (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(100) NOT NULL
);

CREATE TABLE Customers (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(25) NOT NULL
);

CREATE TABLE Rents (
    ID INTEGER PRIMARY KEY,
    BookID INTEGER REFERENCES Books(ID),
    CustomerID INTEGER REFERENCES Customers(ID),
    State VARCHARD(25) NOT NULL
);

-- insertamos los datos en las tablas

INSERT INTO Books (ID, Name, Author)
VALUES (1, 'Don Quijote', 1);
INSERT INTO Books (ID, Name, Author)
VALUES (2, 'La Divina comedia', 2);
INSERT INTO Books (ID, Name, Author)
VALUES (3, 'Vagabond 1-3', 3);
INSERT INTO Books (ID, Name, Author)
VALUES (4, 'Dragon Ball 1', 4);
INSERT INTO Books (ID, Name, Author)
VALUES (5, 'The Book of the 5 Rings', NULL);

INSERT INTO Authors (ID, Name)
VALUES (1, 'Miguel de cervantes');
INSERT INTO Authors (ID, Name)
VALUES (2, 'Dante Alighieri');
INSERT INTO Authors (ID, Name)
VALUES (3, 'Takehiko Inoue');
INSERT INTO Authors (ID, Name)
VALUES (4, 'Akira Toriyama');
INSERT INTO Authors (ID, Name)
VALUES (5, 'Walt Disney');

INSERT INTO Customers (ID, Name, Email)
VALUES (1, 'John Doe', 'j.doe@email.com');
INSERT INTO Customers (ID, Name, Email)
VALUES (2, 'Jane Doe', 'jane@doe.com');
INSERT INTO Customers (ID, Name, Email)
VALUES (3, 'Luke Skywalker', 'darth.son@email.com');

INSERT INTO Rents (ID, BookID, CustomerID, State)
VALUES (1, 1, 2, 'Returned');
INSERT INTO Rents (ID, BookID, CustomerID, State)
VALUES (2, 2, 2, 'Returned');
INSERT INTO Rents (ID, BookID, CustomerID, State)
VALUES (3, 1, 1, 'On time');
INSERT INTO Rents (ID, BookID, CustomerID, State)
VALUES (4, 3, 1, 'On time');
INSERT INTO Rents (ID, BookID, CustomerID, State)
VALUES (5, 2, 2, 'Overdue');

--Obtenga todos los libros y sus autores

SELECT books.Name AS Book, authors.Name AS Author
FROM Books AS books 
LEFT JOIN Authors AS authors 
ON books.Author = authors.ID;

--Obtenga todos los libros que no tienen autor

SELECT Books.ID, Books.Name AS Book 
FROM Books
WHERE Books.Author is NULL;

--Obtenga todos los autores que no tienen libros

SELECT Authors.ID, Authors.Name AS Author
FROM Authors 
LEFT JOIN Books
ON Authors.ID = Books.Author
WHERE Books.ID is NULL;

--Obtenga todos los libros que han sido rentados en algún momento

SELECT DISTINCT Books.ID, Books.Name AS book 
FROM Books
INNER JOIN Rents
ON Books.ID = Rents.BookID

--Obtenga todos los libros que nunca han sido rentados

SELECT Books.ID, Books.Name AS book 
FROM Books
LEFT JOIN Rents
ON Books.ID = Rents.BookID
WHERE Rents.BookID IS NULL;

--Obtenga todos los clientes que nunca han rentado un libro

SELECT Customers.ID, Customers.Name AS customer, Customers. Email
FROM Customers
LEFT JOIN Rents
ON Customers.ID = Rents.CustomerID
WHERE Rents.CustomerID IS NULL;

--Obtenga todos los libros que han sido rentados y están en estado “Overdue”


SELECT Books.ID, Books.Name AS book, Rents.State
FROM Books
INNER JOIN Rents
ON Books.ID = Rents.BookID
WHERE Rents.State = 'Overdue';

