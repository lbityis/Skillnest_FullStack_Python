# ==========================================================
# MODELO MASCOTA
# ==========================================================

from mysqlconnection import connectToMySQL


# ==========================================================
# CLASE MASCOTA
# ==========================================================

class Mascota:
    """
    Representa un registro de la tabla mascotas.
    """

    def __init__(self, data):
        """
        Convierte un diccionario de MySQL en un objeto Mascota.
        """

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
        Devuelve todas las mascotas de la base de datos.
        """

        query = """
            SELECT *
            FROM mascotas;
        """


        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query)


        mascotas = []


        for mascota in resultados:

            mascotas.append(
                cls(mascota)
            )


        return mascotas


    # ======================================================
    # OBTENER MASCOTA POR ID
    # ======================================================

    @classmethod
    def get_by_id(cls, id):
        """
        Busca una mascota utilizando su ID.

        El ID recibido desde Python se envía como parámetro
        de una sentencia preparada.
        """

        # --------------------------------------------------
        # QUERY
        # --------------------------------------------------

        query = """
            SELECT *
            FROM mascotas
            WHERE id = %(id_mascota)s;
        """


        # --------------------------------------------------
        # DATOS VARIABLES
        # --------------------------------------------------

        data = {
            "id_mascota": id
        }


        # --------------------------------------------------
        # EJECUTAR CONSULTA
        # --------------------------------------------------

        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(
            query,
            data
        )


        # --------------------------------------------------
        # COMPROBAR RESULTADO
        # --------------------------------------------------

        if resultados:

            return cls(
                resultados[0]
            )


        return None

# ======================================================
    # OBTENER MASCOTAS POR TIPO (DESAFÍO)
    # ======================================================
    @classmethod
    def get_by_tipo(cls, tipo):
        """
        Busca y retorna todas las mascotas de un determinado tipo.
        Devuelve una lista de objetos Mascota.
        """
        # 1. Definir la consulta con marcador de posición
        query = """
            SELECT *
            FROM mascotas
            WHERE tipo = %(tipo_mascota)s;
        """

        # 2. Definir el diccionario con el valor variable
        data = {
            "tipo_mascota": tipo
        }

        # 3. Ejecutar la consulta en la base de datos
        resultados = connectToMySQL("primera_flask").query_db(query, data)

        # 4. Convertir los diccionarios en objetos Mascota
        mascotas = []
        if resultados:
            for mascota in resultados:
                mascotas.append(cls(mascota))

        return mascotas