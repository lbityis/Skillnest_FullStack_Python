# ==========================================================
# MODELO MASCOTA
# ==========================================================
from mysqlconnection import connectToMySQL

class Mascota:
    """
    Representa un registro de la tabla mascotas.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo = data["tipo"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # ======================================================
    # OBTENER TODAS LAS MASCOTAS
    # ======================================================
    @classmethod
    def get_all(cls):
        """
        Consulta todas las mascotas de la base de datos.
        Retorna una lista de objetos Mascota.
        """
        query = "SELECT * FROM mascotas;"
        resultados = connectToMySQL("primera_flask").query_db(query)

        mascotas = []
        if resultados:
            for mascota in resultados:
                mascotas.append(cls(mascota))

        return mascotas

    # ======================================================
    # OBTENER UNA MASCOTA POR ID (DESAFÍO)
    # ======================================================
    @classmethod
    def get_by_id(cls, id):
        """
        Consulta una mascota específica por su ID.
        Retorna una instancia de Mascota o None si no existe.
        """
        query = "SELECT * FROM mascotas WHERE id = %(id)s;"
        data = {"id": id}

        resultados = connectToMySQL("primera_flask").query_db(query, data)

        # Si encontramos un resultado, creamos y retornamos el objeto Mascota
        if resultados and len(resultados) > 0:
            return cls(resultados[0])

        return None