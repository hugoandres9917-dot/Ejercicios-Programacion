--Lyfter_car_rental
-- Crear esquema y ruta de busquedad
CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;
SET search_path TO lyfter_car_rental;

-- Tipos ENUM para definir estados solo disponiles
CREATE TYPE lyfter_car_rental.status_users AS ENUM ('activo', 'inactivo', 'suspendido', 'moroso');
CREATE TYPE lyfter_car_rental.status_autos AS ENUM ('disponible', 'alquilado', 'mantenimiento', 'deshabilitado');
CREATE TYPE lyfter_car_rental.status_rentals AS ENUM ('activo', 'completado', 'cancelado');

-- Tabla usuarios
CREATE TABLE IF NOT EXISTS lyfter_car_rental.users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    date_birth DATE NOT NULL,
    status lyfter_car_rental.status_users DEFAULT 'activo'
);

-- Tabla automóviles
CREATE TABLE IF NOT EXISTS lyfter_car_rental.vehicles (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    status lyfter_car_rental.status_autos DEFAULT 'disponible'
);

-- Tabla alquileres
CREATE TABLE IF NOT EXISTS lyfter_car_rental.rentals (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES lyfter_car_rental.users(id) ON DELETE CASCADE,
    auto_id INT REFERENCES lyfter_car_rental.vehicles(id) ON DELETE CASCADE,
    rental_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status lyfter_car_rental.status_rentals DEFAULT 'activo'
);

-- Popular 50 usuarios de prueba
INSERT INTO lyfter_car_rental.users (name, email, username, password, date_birth, status) VALUES
('Juan Pérez', 'juan.perez@example.com', 'jperez', 'pass1234', '1990-05-15', 'activo'),
('María López', 'maria.lopez@example.com', 'mlopez', 'pass1234', '1985-08-22', 'activo'),
('Carlos Gómez', 'carlos.gomez@example.com', 'cgomez', 'pass1234', '1992-11-30', 'activo'),
('Ana Rodríguez', 'ana.rodriguez@example.com', 'arodriguez', 'pass1234', '1998-03-10', 'activo'),
('Luis Hernández', 'luis.hernandez@example.com', 'lhernandez', 'pass1234', '1988-12-05', 'inactivo'),
('Sofía Martínez', 'sofia.martinez@example.com', 'smartinez', 'pass1234', '1995-07-19', 'activo'),
('Diego Sánchez', 'diego.sanchez@example.com', 'dsanchez', 'pass1234', '1991-01-25', 'activo'),
('Laura Ramírez', 'laura.ramirez@example.com', 'lramirez', 'pass1234', '1993-09-14', 'suspendido'),
('Javier Flores', 'javier.flores@example.com', 'jflores', 'pass1234', '1987-04-03', 'activo'),
('Lucía Torres', 'lucia.torres@example.com', 'ltorres', 'pass1234', '1996-06-18', 'activo'),
('Fernando Díaz', 'fernando.diaz@example.com', 'fdiaz', 'pass1234', '1989-10-12', 'activo'),
('Elena Vázquez', 'elena.vazquez@example.com', 'evazquez', 'pass1234', '1994-02-28', 'activo'),
('Gabriel Castro', 'gabriel.castro@example.com', 'gcastro', 'pass1234', '1997-12-01', 'activo'),
('Valeria Morales', 'valeria.morales@example.com', 'vmorales', 'pass1234', '1991-08-17', 'inactivo'),
('Ricardo Gutiérrez', 'ricardo.gutierrez@example.com', 'rgutierrez', 'pass1234', '1983-03-24', 'activo'),
('Patricia Ortiz', 'patricia.ortiz@example.com', 'portiz', 'pass1234', '1990-11-09', 'activo'),
('Alejandro Silva', 'alejandro.silva@example.com', 'asilva', 'pass1234', '1986-05-04', 'activo'),
('Camila Ruiz', 'camila.ruiz@example.com', 'cruiz', 'pass1234', '1999-01-15', 'activo'),
('Manuel Núñez', 'manuel.nunez@example.com', 'mnunez', 'pass1234', '1992-07-22', 'moroso'),
('Gabriela Alvarez', 'gabriela.alvarez@example.com', 'galvarez', 'pass1234', '1995-10-30', 'activo'),
('Santiago Romero', 'santiago.romero@example.com', 'sromero', 'pass1234', '1984-09-11', 'activo'),
('Daniela Navarro', 'daniela.navarro@example.com', 'dnavarro', 'pass1234', '1993-04-05', 'activo'),
('Mateo Molina', 'mateo.molina@example.com', 'mmolina', 'pass1234', '1998-08-14', 'activo'),
('Paula Delgado', 'paula.delgado@example.com', 'pdelgado', 'pass1234', '1991-06-20', 'inactivo'),
('Nicolás Aguilar', 'nicolas.aguilar@example.com', 'naguilar', 'pass1234', '1989-02-17', 'activo'),
('Andrea Medina', 'andrea.medina@example.com', 'amedina', 'pass1234', '1997-03-29', 'activo'),
('Emilio Vega', 'emilio.vega@example.com', 'evega', 'pass1234', '1986-12-13', 'activo'),
('Isabel Campos', 'isabel.campos@example.com', 'icampos', 'pass1234', '1994-11-07', 'suspendido'),
('Adrián Vargas', 'adrian.vargas@example.com', 'avargas', 'pass1234', '1990-07-01', 'activo'),
('Monica Castillo', 'monica.castillo@example.com', 'mcastillo', 'pass1234', '1988-10-25', 'activo'),
('Hugo Guzmán', 'hugo.guzman@example.com', 'hguzman', 'pass1234', '1993-05-19', 'activo'),
('Natalia Moreno', 'natalia.moreno@example.com', 'nmoreno', 'pass1234', '1996-09-08', 'activo'),
('Sebastián Muñoz', 'sebastian.munoz@example.com', 'smunoz', 'pass1234', '1991-04-12', 'activo'),
('Claudia Rojas', 'claudia.rojas@example.com', 'crojas', 'pass1234', '1985-01-31', 'inactivo'),
('Jorge Guerrero', 'jorge.guerrero@example.com', 'jguerrero', 'pass1234', '1997-06-23', 'activo'),
('Fernanda Reyes', 'fernanda.reyes@example.com', 'freyes', 'pass1234', '1992-08-04', 'activo'),
('Esteban Peña', 'esteban.pena@example.com', 'epena', 'pass1234', '1987-11-16', 'activo'),
('Carla Herrera', 'carla.herrera@example.com', 'cherrera', 'pass1234', '1995-02-09', 'activo'),
('Rodrigo Cabrera', 'rodrigo.cabrera@example.com', 'rcabrera', 'pass1234', '1990-10-27', 'moroso'),
('Mariana Fuentes', 'mariana.fuentes@example.com', 'mfuentes', 'pass1234', '1998-07-03', 'activo'),
('Gonzalo Valenzuela', 'gonzalo.valenzuela@example.com', 'gvalenzuela', 'pass1234', '1989-03-21', 'activo'),
('Verónica Lara', 'veronica.lara@example.com', 'vlara', 'pass1234', '1994-12-14', 'activo'),
('Felipe Méndez', 'felipe.mendez@example.com', 'fmendez', 'pass1234', '1993-01-08', 'activo'),
('Lorena Cruz', 'lorena.cruz@example.com', 'lcruz', 'pass1234', '1986-06-30', 'inactivo'),
('Marcos León', 'marcos.leon@example.com', 'mleon', 'pass1234', '1997-09-17', 'activo'),
('Jimena Ibarra', 'jimena.ibarra@example.com', 'jibarra', 'pass1234', '1991-11-02', 'activo'),
('Raúl Paredes', 'raul.paredes@example.com', 'rparedes', 'pass1234', '1988-04-26', 'activo'),
('Silvia Soto', 'silvia.soto@example.com', 'ssoto', 'pass1234', '1996-10-05', 'activo'),
('Héctor Figueroa', 'hector.figueroa@example.com', 'hfigueroa', 'pass1234', '1992-02-11', 'activo'),
('Daniela Rivas', 'daniela.rivas@example.com', 'drivas', 'pass1234', '1995-05-28', 'activo');

-- Popular autos de prueba
INSERT INTO lyfter_car_rental.vehicles (brand, model, year, status) VALUES
('Toyota', 'Corolla', 2021, 'disponible'),
('Honda', 'Civic', 2022, 'disponible'),
('Ford', 'Mustang', 2020, 'disponible'),
('Chevrolet', 'Onix', 2023, 'disponible'),
('Nissan', 'Sentra', 2021, 'disponible'),
('Hyundai', 'Elantra', 2022, 'disponible'),
('Kia', 'Rio', 2019, 'deshabilitado'),
('Volkswagen', 'Jetta', 2021, 'disponible'),
('BMW', 'Series 3', 2023, 'disponible'),
('Mazda', 'Mazda 3', 2022, 'disponible');

