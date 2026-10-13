import pymysql.cursors

class ConexionMySQL:
    def __init__(self, bd):
        # Configuracion de la conexion local a MySQL
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="elikiri08", 
            database=bd,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def consultar_bd(self, consulta, datos=None):
        with self.conexion.cursor() as cursor:
            try:
                cursor.execute(consulta, datos or {})
                sql = consulta.strip().lower()

                if sql.startswith("select"):
                    return cursor.fetchall()
                if sql.startswith("insert"):
                    return cursor.lastrowid
                return cursor.rowcount
            except Exception as e:
                print("Error en la consulta SQL:", e)
                return False
            finally:
                self.conexion.close()

def conectar_mysql(bd):
    return ConexionMySQL(bd)