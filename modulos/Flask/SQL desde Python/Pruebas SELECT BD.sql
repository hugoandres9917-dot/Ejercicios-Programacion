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