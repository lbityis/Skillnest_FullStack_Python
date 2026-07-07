from conexion import Conexion

class Usuario:
    def __init__(self, usuario, password, tipo, id=None):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipo = tipo 

    @staticmethod
    def existe_usuario(username):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        
        sql = "SELECT id_usuario FROM usuarios WHERE username = %s AND deleted = 0"
        cursor.execute(sql, (username,))
        resultado = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        return resultado is not None

    def crear(self):
        if Usuario.existe_usuario(self.usuario):
            print(f"\n[Error] El nombre de usuario '{self.usuario}' ya está registrado.")
            return False
            
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
    
        id_tipo = 1 if self.tipo == "ADMIN" else 2
        
        sql = """
        INSERT INTO usuarios (username, password_hash, id_tipo_usuario, created_by)
        VALUES (%s, %s, %s, 'system')
        """
        cursor.execute(sql, (self.usuario, self.password, id_tipo))
        conexion.commit()
        print("\nUsuario agregado correctamente.")
        
        cursor.close()
        conexion.close()
        return True

    @staticmethod
    def buscar_por_id(id_usuario):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        
        sql = "SELECT id_usuario, username, id_tipo_usuario FROM usuarios WHERE id_usuario = %s AND deleted = 0"
        cursor.execute(sql, (id_usuario,))
        resultado = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        return resultado 

    @staticmethod
    def listar():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        
        sql = """
        SELECT u.id_usuario, u.username, t.nombre_tipo 
        FROM usuarios u
        INNER JOIN tipo_usuarios t ON u.id_tipo_usuario = t.id_tipo_usuario
        WHERE u.deleted = 0
        """
        cursor.execute(sql)
        usuarios = cursor.fetchall()
        
        print("\nID   Usuario        Tipo")
        print("---------------------------")
        for u in usuarios:
            tipo_formato = "ADMIN" if u[2] == "Administrador" or u[2] == 1 else "USER"
            print(f"{u[0]}    {u[1]:<14} {tipo_formato}")
            
        print("---------------------------")
        print(f"Total de usuarios registrados: {len(usuarios)}")
        
        cursor.close()
        conexion.close()

    @staticmethod
    def modificar():
        id_usuario = int(input("Modificar usuario ID: "))
        user = Usuario.buscar_por_id(id_usuario)
        
        if user:
            nuevo_user = input("Nuevo usuario: ")
            
            if nuevo_user != user[1] and Usuario.existe_usuario(nuevo_user):
                print(f"\n[Error] El nombre de usuario '{nuevo_user}' ya está en uso.")
                return
                
            nuevo_pass = input("Nueva contraseña: ")
            nuevo_tipo = input("Nuevo tipo (ADMIN o USER): ").upper()
            id_tipo = 1 if nuevo_tipo == "ADMIN" else 2
            
            conexion = Conexion.conectar()
            cursor = conexion.cursor()
            sql = """
            UPDATE usuarios 
            SET username = %s, password_hash = %s, id_tipo_usuario = %s 
            WHERE id_usuario = %s
            """
            cursor.execute(sql, (nuevo_user, nuevo_pass, id_tipo, id_usuario))
            conexion.commit()
            print("\nUsuario modificado correctamente.")
            cursor.close()
            conexion.close()
        else:
            print("\nUsuario no encontrado.")

    @staticmethod
    def eliminar():
        id_usuario = int(input("Eliminar usuario ID: "))
        user = Usuario.buscar_por_id(id_usuario)
        
        if user:
            confirmacion = input(f"¿Estás seguro de que deseas eliminar al usuario '{user[1]}'? (S/N): ").upper()
            if confirmacion == "S":
                conexion = Conexion.conectar()
                cursor = conexion.cursor()
                cursor.execute("UPDATE usuarios SET deleted = 1 WHERE id_usuario = %s", (id_usuario,))
                conexion.commit()
                print("\nUsuario eliminado correctamente.")
                cursor.close()
                conexion.close()
            else:
                print("\nEliminación cancelada.")
        else:
            print("\nUsuario no encontrado.")

    @staticmethod
    def validar_inicio_sesion(usuario, password):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        
        sql = "SELECT id_usuario, username, id_tipo_usuario FROM usuarios WHERE username = %s AND password_hash = %s AND deleted = 0"
        cursor.execute(sql, (usuario, password))
        resultado = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        
        if resultado:
            tipo_str = "ADMIN" if resultado[2] == 1 else "USER"
            return {"id": resultado[0], "usuario": resultado[1], "tipo": tipo_str}
        return None

    @staticmethod
    def cambiar_password(id_usuario, nueva_password):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        
        sql = "UPDATE usuarios SET password_hash = %s WHERE id_usuario = %s"
        cursor.execute(sql, (nueva_password, id_usuario))
        conexion.commit()
        print("\nContraseña actualizada correctamente.")
        
        cursor.close()
        conexion.close()