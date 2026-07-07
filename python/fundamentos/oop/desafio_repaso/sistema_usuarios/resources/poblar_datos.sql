-- =====================================================================
-- ARCHIVO: poblar_datos.sql
-- DESCRIPCIÓN: Inserción de datos iniciales en el sistema.
-- =====================================================================

USE usuarios_db;

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