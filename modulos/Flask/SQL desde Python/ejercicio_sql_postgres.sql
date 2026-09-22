

-- Lyfter_car_rental
-- Crear esquema y definir ruta de búsqueda
CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;
SET search_path TO lyfter_car_rental;

-- 1. ELIMINAR TABLAS PREVIAS (Para forzar recreación limpia) cabios solicitados
DROP TABLE IF EXISTS lyfter_car_rental.rentals CASCADE;
DROP TABLE IF EXISTS lyfter_car_rental.vehicles CASCADE;
DROP TABLE IF EXISTS lyfter_car_rental.users CASCADE;

-- 2. ELIMINAR TIPOS ENUM PREVIOS eliminar los tipos de estados previos 
DROP TYPE IF EXISTS lyfter_car_rental.status_users CASCADE;
DROP TYPE IF EXISTS lyfter_car_rental.status_autos CASCADE;
DROP TYPE IF EXISTS lyfter_car_rental.status_rentals CASCADE;

-- 3. cambio solicitado CREAR TIPOS ENUM CON VALORES EN INGLES
CREATE TYPE lyfter_car_rental.status_users AS ENUM ('active', 'inactive', 'suspended', 'delinquent');
CREATE TYPE lyfter_car_rental.status_autos AS ENUM ('available', 'rented', 'maintenance', 'unavailable');
CREATE TYPE lyfter_car_rental.status_rentals AS ENUM ('active', 'completed', 'cancelled');

-- 4. CREAR TABLAS
CREATE TABLE lyfter_car_rental.users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    date_birth DATE NOT NULL,
    status lyfter_car_rental.status_users DEFAULT 'active'
);

CREATE TABLE lyfter_car_rental.vehicles (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    status lyfter_car_rental.status_autos DEFAULT 'available'
);

CREATE TABLE lyfter_car_rental.rentals (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES lyfter_car_rental.users(id) ON DELETE CASCADE,
    auto_id INT REFERENCES lyfter_car_rental.vehicles(id) ON DELETE CASCADE,
    rental_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status lyfter_car_rental.status_rentals DEFAULT 'active'
);

-- 5. POPULAR USUARIOS DE PRUEBA (EN INGLES)
INSERT INTO lyfter_car_rental.users (name, email, username, password, date_birth, status) VALUES
('Juan Pérez', 'juan.perez@example.com', 'jperez', 'pass1234', '1990-05-15', 'active'),
('María López', 'maria.lopez@example.com', 'mlopez', 'pass1234', '1985-08-22', 'active'),
('Carlos Gómez', 'carlos.gomez@example.com', 'cgomez', 'pass1234', '1992-11-30', 'active'),
('Ana Rodríguez', 'ana.rodriguez@example.com', 'arodriguez', 'pass1234', '1998-03-10', 'active'),
('Luis Hernández', 'luis.hernandez@example.com', 'lhernandez', 'pass1234', '1988-12-05', 'inactive'),
('Sofía Martínez', 'sofia.martinez@example.com', 'smartinez', 'pass1234', '1995-07-19', 'active'),
('Diego Sánchez', 'diego.sanchez@example.com', 'dsanchez', 'pass1234', '1991-01-25', 'active'),
('Laura Ramírez', 'laura.ramirez@example.com', 'lramirez', 'pass1234', '1993-09-14', 'suspended'),
('Javier Flores', 'javier.flores@example.com', 'jflores', 'pass1234', '1987-04-03', 'active'),
('Lucía Torres', 'lucia.torres@example.com', 'ltorres', 'pass1234', '1996-06-18', 'active'),
('Fernando Díaz', 'fernando.diaz@example.com', 'fdiaz', 'pass1234', '1989-10-12', 'active'),
('Elena Vázquez', 'elena.vazquez@example.com', 'evazquez', 'pass1234', '1994-02-28', 'active'),
('Gabriel Castro', 'gabriel.castro@example.com', 'gcastro', 'pass1234', '1997-12-01', 'active'),
('Valeria Morales', 'valeria.morales@example.com', 'vmorales', 'pass1234', '1991-08-17', 'inactive'),
('Ricardo Gutiérrez', 'ricardo.gutierrez@example.com', 'rgutierrez', 'pass1234', '1983-03-24', 'active'),
('Patricia Ortiz', 'patricia.ortiz@example.com', 'portiz', 'pass1234', '1990-11-09', 'active'),
('Alejandro Silva', 'alejandro.silva@example.com', 'asilva', 'pass1234', '1986-05-04', 'active'),
('Camila Ruiz', 'camila.ruiz@example.com', 'cruiz', 'pass1234', '1999-01-15', 'active'),
('Manuel Núñez', 'manuel.nunez@example.com', 'mnunez', 'pass1234', '1992-07-22', 'delinquent'),
('Gabriela Alvarez', 'gabriela.alvarez@example.com', 'galvarez', 'pass1234', '1995-10-30', 'active'),
('Santiago Romero', 'santiago.romero@example.com', 'sromero', 'pass1234', '1984-09-11', 'active'),
('Daniela Navarro', 'daniela.navarro@example.com', 'dnavarro', 'pass1234', '1993-04-05', 'active'),
('Mateo Molina', 'mateo.molina@example.com', 'mmolina', 'pass1234', '1998-08-14', 'active'),
('Paula Delgado', 'paula.delgado@example.com', 'pdelgado', 'pass1234', '1991-06-20', 'inactive'),
('Nicolás Aguilar', 'nicolas.aguilar@example.com', 'naguilar', 'pass1234', '1989-02-17', 'active'),
('Andrea Medina', 'andrea.medina@example.com', 'amedina', 'pass1234', '1997-03-29', 'active'),
('Emilio Vega', 'emilio.vega@example.com', 'evega', 'pass1234', '1986-12-13', 'active'),
('Isabel Campos', 'isabel.campos@example.com', 'icampos', 'pass1234', '1994-11-07', 'suspended'),
('Adrián Vargas', 'adrian.vargas@example.com', 'avargas', 'pass1234', '1990-07-01', 'active'),
('Monica Castillo', 'monica.castillo@example.com', 'mcastillo', 'pass1234', '1988-10-25', 'active'),
('Hugo Guzmán', 'hugo.guzman@example.com', 'hguzman', 'pass1234', '1993-05-19', 'active'),
('Natalia Moreno', 'natalia.moreno@example.com', 'nmoreno', 'pass1234', '1996-09-08', 'active'),
('Sebastián Muñoz', 'sebastian.munoz@example.com', 'smunoz', 'pass1234', '1991-04-12', 'active'),
('Claudia Rojas', 'claudia.rojas@example.com', 'crojas', 'pass1234', '1985-01-31', 'inactive'),
('Jorge Guerrero', 'jorge.guerrero@example.com', 'jguerrero', 'pass1234', '1997-06-23', 'active'),
('Fernanda Reyes', 'fernanda.reyes@example.com', 'freyes', 'pass1234', '1992-08-04', 'active'),
('Esteban Peña', 'esteban.pena@example.com', 'epena', 'pass1234', '1987-11-16', 'active'),
('Carla Herrera', 'carla.herrera@example.com', 'cherrera', 'pass1234', '1995-02-09', 'active'),
('Rodrigo Cabrera', 'rodrigo.cabrera@example.com', 'rcabrera', 'pass1234', '1990-10-27', 'delinquent'),
('Mariana Fuentes', 'mariana.fuentes@example.com', 'mfuentes', 'pass1234', '1998-07-03', 'active'),
('Gonzalo Valenzuela', 'gonzalo.valenzuela@example.com', 'gvalenzuela', 'pass1234', '1989-03-21', 'active'),
('Verónica Lara', 'veronica.lara@example.com', 'vlara', 'pass1234', '1994-12-14', 'active'),
('Felipe Méndez', 'felipe.mendez@example.com', 'fmendez', 'pass1234', '1993-01-08', 'active'),
('Lorena Cruz', 'lorena.cruz@example.com', 'lcruz', 'pass1234', '1986-06-30', 'inactive'),
('Marcos León', 'marcos.leon@example.com', 'mleon', 'pass1234', '1997-09-17', 'active'),
('Jimena Ibarra', 'jimena.ibarra@example.com', 'jibarra', 'pass1234', '1991-11-02', 'active'),
('Raúl Paredes', 'raul.paredes@example.com', 'rparedes', 'pass1234', '1988-04-26', 'active'),
('Silvia Soto', 'silvia.soto@example.com', 'ssoto', 'pass1234', '1996-10-05', 'active'),
('Héctor Figueroa', 'hector.figueroa@example.com', 'hfigueroa', 'pass1234', '1992-02-11', 'active'),
('Daniela Rivas', 'daniela.rivas@example.com', 'drivas', 'pass1234', '1995-05-28', 'active');

-- 6. POPULAR VEHICULOS DE PRUEBA (EN INGLES)
INSERT INTO lyfter_car_rental.vehicles (brand, model, year, status) VALUES
('Toyota', 'Corolla', 2021, 'available'),
('Honda', 'Civic', 2022, 'available'),
('Ford', 'Mustang', 2020, 'available'),
('Chevrolet', 'Onix', 2023, 'available'),
('Nissan', 'Sentra', 2021, 'available'),
('Hyundai', 'Elantra', 2022, 'available'),
('Kia', 'Rio', 2019, 'unavailable'),
('Volkswagen', 'Jetta', 2021, 'available'),
('BMW', 'Series 3', 2023, 'available'),
('Mazda', 'Mazda 3', 2022, 'available');