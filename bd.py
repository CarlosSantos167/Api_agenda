CREATE DATABASE db_agenda
USE DATABASE db_agenda

CREATE TABLE personas(
    id_persona  INT PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(30) NOT NULL,
    primer_apellido VARCHAR(20) NOT NULL,
    segundo_apellido VARCHAR(20) NOT NULL,
    email VARCHAR(30) UNIQUE,
    telefono VARCHAR(12)
);

INSERT INTO personas (nombre, primer_apellido, segundo_apellido, email, telefono) 
VALUES 
('Juan', 'Pérez', 'Gómez', 'juan.perez@example.com', '5551234567'),
('Ana', 'López', 'Martínez', 'ana.lopez@example.com', '5559876543'),
('Carlos', 'García', 'Rodríguez', 'carlos.garcia@example.com', '5557654321')