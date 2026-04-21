-- SQLite
--

--Creamos la tabla Original Empleados y Proyectos

CREATE TABLE EmpleadosyProyectos (
    Employee_ID INTEGER ,
    Employee_Name VARCHAR(100),
    Department VARCHAR(100),
    Department_Phone VARCHAR(20),
    Project_ID TEXT NOT NULL,
    Project_Name VARCHAR(100),
    Project_Buget Decilmal(12,2)
);

INSERT INTO EmpleadosyProyectos (Employee_ID, Employee_Name, Department, Department_Phone, Project_ID, Project_Name, Project_Buget)
VALUES (201, 'Ana Rivera', 'IT', '2222-2222', 'P001', 'Web App', 50000.00);
INSERT INTO EmpleadosyProyectos (Employee_ID, Employee_Name, Department, Department_Phone, Project_ID, Project_Name, Project_Buget)
VALUES (201, 'Ana Rivera', 'IT', '2222-2222', 'P002', 'API REST', 25000.00);
INSERT INTO EmpleadosyProyectos (Employee_ID, Employee_Name, Department, Department_Phone, Project_ID, Project_Name, Project_Buget)
VALUES (202, 'Luis Mendez', 'Marketing', '1111-1111', 'P003', 'Campaña TV', 30000.00);

--(1FN)
--La tabla cumple con 1FN porque cada celda tiene un un solo valor.Department
--hay redundancia

--(2FN)
--No dependencias parciales en claves compuestas
-- el employeename depende de EmployeeID
-- Department y Department phone depende de empleado no de proyecto
--separamos en tablas la tabla original
--tabla Empleado
--tabla Proyecto
--tabla cruz EmpleadoProyecto

CREATE TABLE Empledo (
    Employee_ID INTEGER PRIMARY KEY,
    Employee_Name VARCHAR(100) NOT NULL,
    Department VARCHAR(100),
    Department_Phone  VARCHAR(20)
);

INSERT INTO Empledo(Employee_ID, Employee_Name, Department, Department_Phone)
VALUES (201, 'Ana Rivera', 'IT', '2222-2222');
INSERT INTO Empledo(Employee_ID, Employee_Name, Department, Department_Phone)
VALUES (202, 'Luis Mendez', 'Marketing', '1111-1111');

CREATE TABLE Proyecto (
    Project_ID VARCHAR(10) PRIMARY KEY,
    Project_Name VARCHAR(100) NOT NULL,
    Project_Budget DECIMAL(12,2) NOT NULL
);
INSERT INTO Proyecto (Project_ID, Project_Name, Project_Budget)
VALUES
('P001', 'Web App', 50000.00),
('P002', 'API REST', 25000.00),
('P003', 'Campaña TV', 30000.00);

CREATE TABLE Empleado_Proyecto (
    Employee_ID INTEGER REFERENCES Empledo(Employee_ID),
    Project_ID VARCHAR(10) REFERENCES Proyecto(Project_ID)
);

INSERT INTO Empleado_Proyecto (Employee_ID, Project_ID)
VALUES
(201, 'P001'),
(201, 'P002'),
(202, 'P003');

--la regla de la tercera forma normal
--3FN
--Dependencias transitivas
-- en la tabla empleados, el department phone depende del department no del empleado
--por eso en este caso la solucion es separar departamentos en otra tabla

--separacion de departamento a empleados ya que numero de telefono depende del departamento y no del empleado

--creamos tabla Departamentos

CREATE TABLE Departamento (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Department_Name VARCHAR(100) NOT NULL UNIQUE,
    Department_Phone VARCHAR(20)
);

INSERT INTO Departamento (Department_Name, Department_Phone)
VALUES ('IT', '2222-2222');
INSERT INTO Departamento (Department_Name, Department_Phone)
VALUES ('Marketing', '1111-1111'); 

--y debemos cambiar la estrutura de la tabla empleado por eso la vamos a eliminar y luego crear con los nuevos cambios 
-- el cual es por medio de departmentid podemos referenciar al departamento

DROP TABLE Empledo


CREATE TABLE Empleado (
    ID INTEGER PRIMARY KEY,
    Employee_Name VARCHAR(100) NOT NULL,
    Department_Id INTEGER REFERENCES Departamento(ID)
);

INSERT INTO Empleado (ID, Employee_Name, Department_Id)
VALUES (201, 'Ana Rivera', 1);
INSERT INTO Empleado (ID, Employee_Name, Department_Id)
VALUES (202, 'Luis Mendez', 2);

--- con este diseño
--Departamento se crea con un ID propio para evitar dependencias transitivas
--Empleado referencia al departamento mediante Department Id
--Proyecto cada uno tiene su propio presupuesto y nombre dependientes solo de Project_ID
--Empleado_Proyecto tabla cruz para manejar la realcion entre empleado y Proyecto

---------------------------------------------------------


--segundo ejercicio tabla Registro de Clases

--(1FN)
--La tabla cumple con la Primera regla
--ya que cada celda tiene un solo valor

--Tabla registro de clase 

CREATE TABLE Registro_Clases (
    Student_Id INTEGER,
    Student_Name VARCHAR(100) NOT NULL,
    CourseCode VARCHAR(10)  NOT NULL,
    Course_Name VARCHAR(100) NOT NULL,
    Instructor_Name VARCHAR(100) NOT NULL,
    Instructor_Email VARCHAR(100) NOT NULL
);

INSERT INTO Registro_Clases (Student_Id, Student_Name, CourseCode, Course_Name, Instructor_Name, Instructor_Email)
VALUES 
(301, 'Marco Gómez', 'CS101', 'Python I', 'Juan Pérez', 'juan@uni.edu'),
(301, 'Marco Gómez', 'CS102', 'Python II', 'Laura Rojas', 'laura@uni.edu'),
(302, 'Carla Ruiz', 'CS101', 'Python I', 'Juan Pérez', 'juan@uni.edu');



-----------------------------------------------------------

--La (2FN)

-- Estudiante contiene solo atributos dependientes de Estudiante(ID)
--Curso contiene atributos dependientes de CourseCode
--Estudiante_Curso elimina redundancia al manejar relacion N:N
--entre Estudiantes y cursos

--tabla Estudiante
CREATE TABLE Estudiante (
    ID INTEGER PRIMARY KEY,
    Student_Name VARCHAR(100) NOT NULL
);

INSERT INTO Estudiante (ID, Student_Name)
VALUES (301, 'Marco Gomez');
INSERT INTO Estudiante (ID, Student_Name)
VALUES (302, 'Carla Ruiz');


--Tabla Curso


CREATE TABLE Curso (
    CourseCode VARCHAR(10) PRIMARY KEY,
    Course_Name VARCHAR(100),
    Instructor_Name VARCHAR(100),
    Instructor_Email VARCHAR(100)   
);

INSERT INTO Curso (CourseCode, Course_Name, Instructor_Name, Instructor_Email)
VALUES ('CS101', 'Python I', 'Juan Perez', 'juan@uni.edu');
INSERT INTO Curso (CourseCode, Course_Name, Instructor_Name, Instructor_Email)
VALUES ('CS102', 'Python II', 'Laura Rojas', 'laura@uni.edu');

--Tabla Estudiante_Curso

CREATE TABLE Estudiante_Curso (
    Student_Id INTEGER REFERENCES Estudiante(ID),
    CourseCode VARCHAR(10) REFERENCES Curso(CourseCode)
);

INSERT INTO Estudiante_Curso (Student_Id, CourseCode)
VALUES (301, 'CS101');
INSERT INTO Estudiante_Curso (Student_Id,CourseCode)
VALUES (301, 'CS102');
INSERT INTO Estudiante_Curso (Student_Id, CourseCode)
VALUES (302, 'CS101');


--- REGLA (3FN)
---Separamos la informacion de intructor en una tabla adiconal
-- porque el correo depende del instructor no del curso
--modificamos la tabla curso para que haga referencia al instructor mediante Instructor_Id
--Estudiante cada alumno con su ID 
--Estudiante_Curso tabla cruz maneja la relacion N:N entre estudiantes y cursos

--Tabla Instructor

CREATE TABLE Instructor (
    ID INTEGER PRIMARY KEY,
    Instructor_Name VARCHAR(100),
    Instructor_Email VARCHAR(100)
);

INSERT INTO Instructor (ID, Instructor_Name, Instructor_Email)
VALUES (1, 'Juan Perez', 'Juan@uni.edu');
INSERT INTO Instructor (ID, Instructor_Name, Instructor_Email)
VALUES (2, 'Laura Rojas', 'laura@uni.edu');


--Tabla Curso (modificada)
--eliminamos la tabla ya existente y creamos la nueva


DROP TABLE Curso

--NUEVA TABLA CURSO

CREATE TABLE Curso (
    Course_Code VARCHAR(10) PRIMARY KEY,
    Course_Name VARCHAR(100),
    Instructor_Id INTEGER REFERENCES Instructor(ID)
);

INSERT INTO Curso (Course_Code, Course_Name, Instructor_Id)
VALUES ('CS101', 'Python I', 1);
INSERT INTO Curso (Course_Code, Course_Name, Instructor_Id)
VALUES ('CS102', 'Python II', 2);

--tabla Estudiante
CREATE TABLE Estudiante (
    ID INTEGER PRIMARY KEY,
    Student_Name VARCHAR(100) NOT NULL
);
INSERT INTO Estudiante (ID, Student_Name)
VALUES (301, 'Marco Gomez');
INSERT INTO Estudiante (ID, Student_Name)
VALUES (302, 'Carla Ruiz');



--Tabla Estudiante_Curso

CREATE TABLE Estudiante_Curso (
    Student_Id INTEGER REFERENCES Estudiante(ID),
    CourseCode VARCHAR(10) REFERENCES Curso(CourseCode)
);
INSERT INTO Estudiante_Curso (Student_Id, CourseCode)
VALUES (301, 'CS101');
INSERT INTO Estudiante_Curso (Student_Id,CourseCode)
VALUES (301, 'CS102');
INSERT INTO Estudiante_Curso (Student_Id, CourseCode)
VALUES (302, 'CS101');

-----------------------------------------------------------------------------


--tercer ejercicio extra hospital y citas medicas

--tabla original
CREATE TABLE Hospital_Citasmedicas (
    AppointmentID TEXT PRIMARY KEY,
    PatientName TEXT,
    PatientPhone TEXT,
    DoctorName TEXT,
    Specialty TEXT,
    Date TEXT,
    Time TEXT
);
INSERT INTO Hospital_Citasmedicas (AppointmentID, PatientName, PatientPhone, DoctorName, Specialty, Date, Time)
VALUES ('A01', 'Diana Vargas', '8888-1111', 'Dr. Soto', 'Pediatría', '2024-08-01', '10:00 AM');
INSERT INTO Hospital_Citasmedicas (AppointmentID, PatientName, PatientPhone, DoctorName, Specialty, Date, Time)
VALUES ('A02', 'Diana Vargas', '8888-1111', 'Dr. Soto', 'Pediatría', '2024-08-10', '10:00 AM');
INSERT INTO Hospital_Citasmedicas (AppointmentID, PatientName, PatientPhone, DoctorName, Specialty, Date, Time)
VALUES ('A03', 'Edwin Mora', '8999-2222', 'Dr. Mora', 'Cardiología', '2024-08-05', '01:00 PM');

--La tabla original ya cumple con 1FN, lois valores son atomicos
--paso siguiente 2FN, problemas de redundancia
--separamos en tablas
--PatientName y PatientPhone dependen de paciente
--DoctorName y Specialty dependen solo del doctor 
--Appointment tabla cruz entre paciente y doctor

--tabla paciente

CREATE TABLE Paciente (
    PatientID INTEGER PRIMARY KEY,
    PatientName VARCHAR(100),
    PatientPhone VARCHAR(20)
);
INSERT INTO Paciente (PatientID, PatientName, PatientPhone)
VALUES (1, 'Diana Vargas', '8888-1111');
INSERT INTO Paciente (PatientID, PatientName, PatientPhone)
VALUES (2, 'Edwin Mora', '8998-2222');

--tabla Doctor

CREATE TABLE Doctor (
    DoctorID INTEGER PRIMARY KEY,
    DoctorName VARCHAR(100),
    Specialty VARCHAR(100)
);
INSERT INTO Doctor ( DoctorID, DoctorName, Specialty)
VALUES (1, 'Dr. Soto', 'Pediatra');
INSERT INTO Doctor ( DoctorID, DoctorName, Specialty)
VALUES (2, 'Dr. Mora', 'Cardiologia');

--Tabla Appointment

CREATE TABLE Appointment (
    AppointmentID VARCHAR(10) PRIMARY KEY,
    PatientID INTEGER REFERENCES Paciente(PatientID),
    DoctorID INTEGER REFERENCES Doctor(DoctorID),
    Date DATE,
    Time VARCHAR(10)
);
INSERT INTO Appointment (AppointmentID, PatientID, DoctorID, Date, Time)
VALUES ('A01', 1, 1, '2024-08-01', '10:00 AM');
INSERT INTO Appointment (AppointmentID, PatientID, DoctorID, Date, Time)
VALUES ('A02', 1, 1, '2024-08-10', '10:00 AM');
INSERT INTO Appointment (AppointmentID, PatientID, DoctorID, Date, Time)
VALUES ('A03', 2, 2, '2024-08-05', '01:00 PM');

--- TERCERA FORMA NORMAL 3FN
--ya cumple con la regla 3FN ya que

--Paciente tiene datos unicos del Paciente
--Doctor tiene datos unicos tambien
--appointmet es la relacion entre ellos con datos adicionales de la cita










