from flask_app.config.mysqlconnection import conectar_mysql

class Estudiante:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.edad = datos['edad']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']
        self.curso_id = datos['curso_id']

    @classmethod
    def guardar(cls, datos):
        # Inserta un nuevo alumno asignado a un curso
        query = """
            INSERT INTO estudiantes (nombre, apellido, edad, curso_id)
            VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s);
        """
        return conectar_mysql("esquema_estudiantes_cursos").consultar_bd(query, datos)