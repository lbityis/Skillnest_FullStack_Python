import os
from usuario import Usuario

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    limpiar_consola()
    print("==============================")
    print("      SISTEMA DE USUARIOS     ")
    print("==============================")
    print("1. Iniciar sesión")
    print("2. Salir")
    print("==============================")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        limpiar_consola()
        username = input("Usuario: ")
        password = input("Contraseña: ")
        sesion = Usuario.validar_inicio_sesion(username, password)
        
        if sesion:
            # ================= MENÚ ADMINISTRADOR =================
            if sesion["tipo"] == "ADMIN":
                while True:
                    limpiar_consola()
                    print("==============================")
                    print(f"Bienvenido Administrador:\n{sesion['usuario']}\n")
                    print("1. Registrar usuario")
                    print("2. Listar usuarios")
                    print("3. Buscar usuario")
                    print("4. Modificar usuario")
                    print("5. Eliminar usuario")
                    print("6. Cambiar mi contraseña")
                    print("7. Cerrar sesión")
                    print("==============================")
                    
                    opc_admin = input("Selecciona una opción: ")
                    
                    if opc_admin == "1":
                        limpiar_consola()
                        u = input("Usuario: ")
                        p = input("Contraseña: ")
                        t = input("Tipo (ADMIN o USER): ").upper()
                        
                        nuevo_usuario = Usuario(u, p, t)
                        nuevo_usuario.crear()
                        input("\nPresiona Enter para continuar...")
                        
                    elif opc_admin == "2":
                        limpiar_consola()
                        Usuario.listar()
                        input("\nPresiona Enter para continuar...")
                        
                    elif opc_admin == "3":
                        limpiar_consola()
                        try:
                            id_buscar = int(input("Introduce el ID: "))
                            res = Usuario.buscar_por_id(id_buscar)
                            if res:
                                t_str = "ADMIN" if res[2] == 1 else "USER"
                                print(f"\nID: {res[0]}\nUsuario: {res[1]}\nTipo: {t_str}")
                            else:
                                print("\nUsuario no encontrado.")
                        except ValueError:
                            print("\nID inválido.")
                        input("\nPresiona Enter para continuar...")
                        
                    elif opc_admin == "4":
                        limpiar_consola()
                        Usuario.modificar()
                        input("\nPresiona Enter para continuar...")
                        
                    elif opc_admin == "5":
                        limpiar_consola()
                        Usuario.eliminar()
                        input("\nPresiona Enter para continuar...")
                        
                    elif opc_admin == "6":
                        limpiar_consola()
                        nueva_p = input("Introduce tu nueva contraseña: ")
                        Usuario.cambiar_password(sesion["id"], nueva_p)
                        input("\nPresiona Enter para continuar...")
                        
                    elif opc_admin == "7":
                        break 
            # ================= MENÚ USUARIO REGULAR =================
            elif sesion["tipo"] == "USER":
                while True:
                    limpiar_consola()
                    print("==============================")
                    print(f"Bienvenido\n\n{sesion['usuario']}\n")
                    print("Tipo de usuario:\nUSER\n")
                    print("1. Cambiar mi contraseña")
                    print("2. Cerrar sesión")
                    print("==============================")
                    
                    opc_user = input("Selecciona una opción: ")
                    if opc_user == "1":
                        limpiar_consola()
                        nueva_p = input("Introduce tu nueva contraseña: ")
                        Usuario.cambiar_password(sesion["id"], nueva_p)
                        input("\nPresiona Enter para continuar...")
                    elif opc_user == "2":
                        break 
                        
        else:
            print("\nUsuario o contraseña incorrectos.")
            input("\nPresiona Enter para volver al menú inicial...")

    elif opcion == "2":
        limpiar_consola()
        print("Saliendo del sistema...")
        break