from flask_app.config.mysqlconnection import conectar_mysql

class Curso:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']
        # Lista para guardar a los estudiantes del curso
        self.estudiantes = []

    @classmethod
    def obtener_todos(cls):
        query = "SELECT * FROM cursos ORDER BY nombre;"
        resultados = conectar_mysql("esquema_estudiantes_cursos").consultar_bd(query)
        
        cursos = []
        if resultados:
            for fila in resultados:
                cursos.append(cls(fila))
        return cursos

    @classmethod
    def guardar(cls, datos):
        query = "INSERT INTO cursos (nombre) VALUES (%(nombre)s);"
        return conectar_mysql("esquema_estudiantes_cursos").consultar_bd(query, datos)

    @classmethod
    def obtener_con_estudiantes(cls, curso_id):
        # Importamos aqui dentro para evitar que se trave por importacion circular
        from flask_app.models.estudiante import Estudiante

        query = """
            SELECT c.id AS curso_id, c.nombre AS curso_nombre, c.created_at AS curso_created, c.updated_at AS curso_updated,
                   e.id AS estudiante_id, e.nombre AS estudiante_nombre, e.apellido AS estudiante_apellido, 
                   e.edad AS estudiante_edad, e.created_at AS estudiante_created, e.updated_at AS estudiante_updated
            FROM cursos c
            LEFT JOIN estudiantes e ON c.id = e.curso_id
            WHERE c.id = %(id)s;
        """
        datos = {"id": curso_id}
        resultados = conectar_mysql("esquema_estudiantes_cursos").consultar_bd(query, datos)

        if not resultados:
            return None

        # Instanciamos el curso con la primera fila obtenida
        curso = cls({
            "id": resultados[0]["curso_id"],
            "nombre": resultados[0]["curso_nombre"],
            "created_at": resultados[0]["curso_created"],
            "updated_at": resultados[0]["curso_updated"]
        })

        # Agregamos los alumnos si es que existen en el curso
        for fila in resultados:
            if fila["estudiante_id"] is not None:
                datos_estudiante = {
                    "id": fila["estudiante_id"],
                    "nombre": fila["estudiante_nombre"],
                    "apellido": fila["estudiante_apellido"],
                    "edad": fila["estudiante_edad"],
                    "created_at": fila["estudiante_created"],
                    "updated_at": fila["estudiante_updated"],
                    "curso_id": curso.id
                }
                curso.estudiantes.append(Estudiante(datos_estudiante))

        return curso