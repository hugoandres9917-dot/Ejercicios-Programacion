#Pruebas para la base de datos ejecicio_sql_postgres

SET search_path TO lyfter_car_rental;

-- 1. Consultar todos los usuarios y sus estados (filtrando por 'active')
SELECT id, name, email, status 
FROM lyfter_car_rental.users 
WHERE status = 'active';

-- 2. Consultar vehículos disponibles
SELECT id, brand, model, year, status 
FROM lyfter_car_rental.vehicles 
WHERE status = 'available';

-- 3. Ver el conteo de usuarios agrupados por cada estado ENUM
SELECT status, COUNT(*) AS total 
FROM lyfter_car_rental.users 
GROUP BY status;

-- 4. Ver el conteo de vehículos agrupados por estado
SELECT status, COUNT(*) AS total 
FROM lyfter_car_rental.vehicles 
GROUP BY status;

####################################################################################

##preubas para ejercicios extra

SET search_path TO lyfter_car_rental;

--Nivel 1: Filtros y Agregaciones Básicas
--1. Usuarios activos nacidos después del año 2000
--Obtén el nombre, correo y fecha de nacimiento de los usuarios con estado 'active' nacidos a partir del 1 de enero de 2001.

SELECT name, email, date_birth
FROM users
WHERE status = 'active' 
  AND date_birth >= '2001-01-01'
ORDER BY date_birth DESC;

--2. Conteo de vehículos por marca
--Cuenta cuántos vehículos hay de cada marca y muéstralos ordenados de mayor a menor.

SELECT brand, COUNT(*) AS total_vehiculos
FROM vehicles
GROUP BY brand
ORDER BY total_vehiculos DESC;.

--Nivel 2: Joins (Relaciones entre Tablas)
--3. Historial detallado de alquileres
--Une la tabla rentals con users y vehicles para mostrar el nombre del cliente, la marca y modelo del auto, y la fecha del alquiler.

SELECT 
    r.id AS rental_id,
    u.name AS cliente,
    u.email,
    v.brand AS marca,
    v.model AS modelo,
    r.rental_date,
    r.status AS estado_alquiler
FROM rentals r
JOIN users u ON r.user_id = u.id
JOIN vehicles v ON r.auto_id = v.id
ORDER BY r.rental_date DESC
LIMIT 15;

--4. Top 5 usuarios con más alquileres realizados
--Identifica a los clientes más frecuentes usando GROUP BY con un JOIN.

SELECT 
    u.id,
    u.name AS cliente,
    COUNT(r.id) AS total_alquileres
FROM users u
JOIN rentals r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY total_alquileres DESC
LIMIT 5;

--Nivel 3: Subconsultas y Casos Avanzados
--5. Vehículos que NUNCA han sido alquilados
--Encuentra autos en la base de datos que no tengan ningún registro en la tabla rentals.

SELECT v.id, v.brand, v.model, v.status
FROM vehicles v
LEFT JOIN rentals r ON v.id = r.auto_id
WHERE r.id IS NULL;

--6. Porcentaje de alquileres por estado
--Calcula la cantidad y el porcentaje que representa cada estado de alquiler (active, completed, cancelled).

SELECT 
    status,
    COUNT(*) AS cantidad,
    ROUND((COUNT(*)::decimal / (SELECT COUNT(*) FROM rentals)) * 100, 2) AS porcentaje
FROM rentals
GROUP BY status;