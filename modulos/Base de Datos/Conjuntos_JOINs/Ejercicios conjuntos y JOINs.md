
Ejercicios de Teoría de Conjuntos
Utilizando los siguientes conjuntos

--All = {1,2,3,4,5,6,7,8,9,10}
--Even = {2,4,6,8,10}
--Odd = {1,3,5,7,9}

Realice las siguientes operaciones:

--Even U Odd {2, 4, 6, 8, 10, 1, 3, 5, 7, 9}
--Even ∩ Odd { }
--All - Odd { 2, 4, 6, 8, 10}
--C(Even)  { 1, 3, 5, 7, 9}
--C(Odd-All) { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

Ejercicios de JOINs

1. Investigue y busque documentación
sobre el SELECT que explique cómo utilizar las funcionalidades 
de ORDER BY, LIMIT, GROUP BY y tres tipos de JOIN, y cree una 
tabla (informativa, no de SQL) a partir de sus descubrimientos.

--La sentencia select en SQL permite recuperar, filtrar
--agrupar y ordenar datos de una o varias tablas.
-- 4 clasulas clave. ORDER BY (ordena), LIMIT(restringe filas), GRUOP BY (agrupa) y JOIN (une tablas).

--funcion de SQL SELECT

--ORDER BY: Ordena el resultado de la consulta. se usa ASC O DESC por defecto (ascendente, descendente)

--LIMIT: Restringe el numero de filas devueltas suele ir al final de la consulta

--GROUP BY: Agrupa filas que tienen los mismos valores en columnas
--especificas. usualmente en funciones de agregacion( SUM, COUNT, AVG)

--JOINs: combinan columnas de varias tablas basadas en claves relacionadas
    
    --INNER JOIN: Devuelve solo filas donde hay coincidencia en ambas tablas.
    
    --LEFT JOIN: devuelve todas las filas de la tabla izquierda y coincidencias con la derecha.

    --RIGHT JOIN: Devuelve todas las filas de la tabla derecha y las coincidencias de la  izquierda.


| Funcionalidad | Descripción | Sintaxis básica |
|---------------|-------------|-----------------|
| ORDER BY      | Ordena resultados | SELECT * FROM tabla ORDER BY col ASC  OR DESC; |
| LIMIT         | Limita filas | SELECT * FROM tabla LIMIT 5; |
| GROUP BY      | Agrupa registros | SELECT col, SUM(x) FROM tabla GROUP BY col; |
| INNER JOIN    | Coincidencias en ambas tablas | SELECT a.col, b.col FROM A INNER JOIN B ON A.id = B.id; |
| LEFT JOIN     | Todo lo de la izquierda y coincidencias | SELECT a.col, b.col FROM A LEFT JOIN B ON A.id = B.id; |
| RIGHT JOIN    | Todo lo de la derecha y coincidencias | SELECT a.col, b.col FROM A RIGHT JOIN B ON A.id = B.id; |

--para ver tabla hacer ctrl + shift + v . 