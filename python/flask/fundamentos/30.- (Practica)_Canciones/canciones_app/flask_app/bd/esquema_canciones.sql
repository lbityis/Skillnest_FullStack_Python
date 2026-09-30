-- -----------------------------------------------------
-- Crear base de datos / Esquema
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS `esquema_canciones` 
DEFAULT CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE `esquema_canciones`;

-- -----------------------------------------------------
-- Tabla: usuarios
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `contrasena` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Tabla: canciones
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `canciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NOT NULL,
  `artista` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------
-- Tabla: favoritos (Tabla intermedia)
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `favoritos` (
  `usuario_id` INT NOT NULL,
  `cancion_id` INT NOT NULL,
  PRIMARY KEY (`usuario_id`, `cancion_id`),
  INDEX `fk_favoritos_canciones_idx` (`cancion_id` ASC),
  CONSTRAINT `fk_favoritos_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `usuarios` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_favoritos_canciones`
    FOREIGN KEY (`cancion_id`)
    REFERENCES `canciones` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;