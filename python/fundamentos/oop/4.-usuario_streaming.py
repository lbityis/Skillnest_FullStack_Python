class UsuarioStreaming:
   def __init__(self, nombre, email, suscripcion="Gratis"):
       self.nombre = nombre
       self.email = email
       self.suscripcion = suscripcion
       self.lista_reproduccion = []

elisa = UsuarioStreaming("Elisa", "elisa@gmail.com")
sergio = UsuarioStreaming("Sergio", "sergio@gmail.com")
matias = UsuarioStreaming("Matias", "matias@gmail.com")

def agregar_a_lista(self, contenido):
    """Agrega un contenido a la lista de reproducción del usuario."""
    self.lista_reproduccion.append(contenido)


def ver_contenido(self, titulo):
    """Simula que el usuario reproduce un contenido."""
    


def cambiar_suscripcion(self, nueva_suscripcion):
    """Cambia el tipo de suscripción del usuario."""
    


def mostrar_info_usuario(self):
       """Muestra la información del usuario y su lista de reproducción."""
       pass
   
   # Todos los valores que se deben registrar debe ser con input
   # Añadir unmenu while para llamar a los métodos
   # (Menú de selección)

continuar = True
while continuar:

    print("\n---Ejercicios Python---")
    print("--- 1.- Ejercicio 1 ---")
    print("--- 2.- Ejercicio 2 ---")
    print("--- 3.- Ejercicio 3 ---")
    print("--- 4.- Ejercicio 4 ---")

    opcion = input("\n----Elige una opcion: (1 - 4) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        contenido = input("Agrega un contenido a tu lista de reproducción: ")
        resultado = agregar_a_lista(elisa, contenido)
        print(f"lista de reproducción: {elisa.lista_reproduccion}")
    elif opcion == "2":
        print("\nEjecutando ejercicio 2: ")
        print()
    elif opcion == "3":
        print("\nEjecutando ejercicio 3: ")
        suscripcion = input("Cambiar suscripción: ")
        result = cambiar_suscripcion(sergio, suscripcion)
        print(f"nueva suscripcion: ")
    elif opcion == "4":
        print("\nEjecutando ejercicio 4: ")
        print()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no valida, intenta otra vez")