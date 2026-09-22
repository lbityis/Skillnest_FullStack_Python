-- ==========================================================
-- TABLA USUARIOS
-- ==========================================================
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    edad INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ==========================================================
-- DATOS DE PRUEBA USUARIOS
-- ==========================================================
INSERT INTO usuarios (nombre, email, edad) VALUES
    ("Ana Gómez", "ana@example.com", 28),
    ("Carlos Pérez", "carlos@example.com", 35),
    ("María López", "maria@example.com", 22);