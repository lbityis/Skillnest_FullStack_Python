# Sistema para Controlar Usuarios (CRUD)

## ¿De qué trata este proyecto?
* Es un programa para la consola hecho con Python. Sirve para registrar usuarios y controlar quién entra al sistema. Usando POO (Programación Orientada a Objetos) y se conecta a una base de datos para guardar todo.

## Lo que hace el programa
* **Tiene dos tipos de cuenta (Roles):** 

* **ADMIN:** El que puede hacer todo. Puede registrar usuarios nuevos, ver la lista completa (y cuántos van en total), buscar a alguien por su ID, cambiar datos y borrar usuarios (pero con un borrado lógico).
* **USER:** Una pantalla más simple para los usuarios normales, donde solo pueden ver y mover sus propias cosas.

* No se duplican los nombres: Si intentas registrar a alguien con un nombre que ya existe, el programa te frena para que no haya choques.
* Pregunta antes de borrar: Para que no borres a nadie por accidente, el programa te pide confirmar si de verdad quieres darle cuello al usuario.
* Cambio de contraseña rápido: Si estás logueado, puedes cambiar tu contraseña ahí mismo sin dar tantas vueltas.

## ¿Qué usé para programarlo?
* **El lenguaje:** Python 3.x
* **La base de datos:** MySQL o PostgreSQL (el que prefieras usar).
* limpiar la pantalla de la consola (cls en Windows / clear en Mac o Linux) y que no se vea todo amontonado.

## Cómo ponerlo a funcionar
* **Antes de empezar:**
* Tener instalado Python 3.7 o uno más nuevo.
* programa de base de datos (como MySQL Workbench).

### 1. Crear las Tablas y poblar datos: SQL
* Copiar y pegar el siguiente codigo en MySQL Workbench

DROP DATABASE IF EXISTS usuarios_db;
CREATE DATABASE usuarios_db;
USE usuarios_db;

CREATE TABLE tipo_usuarios (
    id_tipo_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_tipo VARCHAR(50) NOT NULL,
    descripcion_tipo VARCHAR(150) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by VARCHAR(50),
    updated_by VARCHAR(50),
    deleted TINYINT DEFAULT 0
);

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    id_tipo_usuario INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by VARCHAR(50),
    updated_by VARCHAR(50),
    deleted TINYINT DEFAULT 0,
    FOREIGN KEY (id_tipo_usuario) REFERENCES tipo_usuarios (id_tipo_usuario)
);

INSERT INTO tipo_usuarios (nombre_tipo, descripcion_tipo, created_by) VALUES
('Administrador', 'Acceso total al sistema', 'system'),
('Regular', 'Usuario regular', 'system');

INSERT INTO usuarios (username, password_hash, id_tipo_usuario, created_by, updated_by) VALUES
('carlos_admin', 'superadmin2026', 1, 'system', 'system'),
('marta_sys', 'rootpassword', 1, 'system', 'system'),
('soporte_tech', 'admin.support', 1, 'system', 'system'),
('juan_perez', 'user123', 2, 'registro_web', 'registro_web'),
('lucia_gomez', 'password987', 2, 'registro_web', 'registro_web'),
('diego_m', 'mi_clave_secreta', 2, 'registro_web', 'registro_web');

### 2. Conectar el programa a la Base de Datos: Python
* En el archivo conexion.py cambiar los datos para que coincidan con su servidor. El archivo se ve más o menos así:

import mysql.connector

class Conexion:
    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="tu_base_de_datos"
        )

### 3. Probar
* Ya al tener la base de datos lista y la conexión bien hecha, abrir la terminal dentro de la carpeta del proyecto y arráncalo con este comando: python main.py