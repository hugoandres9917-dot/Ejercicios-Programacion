-- ejercicios extra Conjuntos y JOINs

--1.explicación cruzada entre conjuntos y SQL
--Analice la operación de conjuntos All - Odd.
--Explique cómo una operación similar se puede representar en SQL con JOINs.
--¿Qué tipo de JOIN usaría?

Segun lo investigado
En teoria de conjuntos, All - Odd significa "Todos los elementos del conjunto All excepto los
que estan en Odd. como resultado el conjunto de numeros pares.

Equivalente en SQL: una operacion similar se logra con JOINs 
el mas correcto para el caso es el LEFT JOIN + WHERE IS NULL
por que refleja la idea de tomar todo de All y restar lo que coincide con Odd.

--2.Agrupamiento y conteo cruzado
--  Usando las tablas de Books, Customers y Rents:
--  Obtenga el número total de veces que cada cliente ha rentado un libro
--  Ordene de mayor a menor y limite el resultado a los 3 clientes más activos
--  Debe usar: GROUP BY, COUNT(), ORDER BY, LIMIT

SELECT customer.Name AS Customer,
COUNT(rents.BookID) AS Total_Rents --cuenta cuantas veces un libro apararece rentado
FROM Customers customer 
INNER JOIN Rents rents --INNER JOIN para relacionar Customer con Rents y obtener las rentas relacionadas a cada cliente
    ON customer.ID = rents.CustomerID
GROUP BY customer.Name --agrupa los resultados por cliente. para que el COUNT funcione
ORDER BY Total_Rents DESC --ordena la lista de modo menor a mayor
LIMIT 3; --limita el resultado a 3 clientes activos 


--3. Consulta con múltiples JOINS anidados
--  Genere un SELECT que devuelva lo siguiente: 
--  Nombre del cliente
--  Nombre del libro
--  Nombre del autor
--  Estado del alquiler (Rents.State)
--  Debe manejar el caso en que un libro no tenga autor

SELECT customer.Name AS Customer,
book.Name AS Book,
author.Name AS Author,
rents.State AS State
FROM Customers customer 
INNER JOIN Rents rents --une clientes con sus rentas
    ON customer.ID = rents.CustomerID
INNER JOIN Books book   -- une cada renta con el libro correspondiente
    ON rents.BookID = book.ID
LEFT JOIN Authors Author-- une libro con autores, left join en caso de que algun libro no tenga autor osea sea NULL. 
    ON book.Author = author.ID;

    