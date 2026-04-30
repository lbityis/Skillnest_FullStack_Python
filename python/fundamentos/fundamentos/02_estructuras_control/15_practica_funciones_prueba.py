import os
"""Requisitos obligatorios
Su trabajo debe cumplir con lo siguiente:
Uso de funciones con parámetros
Uso de menú con ciclo while
Uso de input() para solicitar datos
Uso de listas (arreglos)
Uso de diccionarios
Uso de ciclos for
Uso de estructuras condicionales (if, elif, else)
Código ordenado, comentado y correctamente indentado
Opción de salida del programa (0. Salir)"""


# Ejercicios a desarrollar

# Su programa deberá considerar las siguientes funciones:

"""1.- Crear una función que reciba una lista de números enteros y muestre 
 cuál es el número mayor y cuál es el menor."""
def listaNum(listado):
    menor = min(listado)
    mayor = max(listado)
    print(f"El número mayor es {mayor} \nEl número menor es {menor}")

def ejercicio1():
    limit = int(input("Ingresa un limite de valores: "))
    listadoNum = []
    i = 1
    while i <= limit:
        num = int(input(f"Ingresa un número entero {i} de {limit} : "))
        listadoNum.append(num)
        i += 1
    listaNum(listadoNum)

""" 2.- Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene."""
def contadorVocales(frase):
    texto = frase.lower()
    vocales = 0
    for i in texto:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
            vocales += 1
    print(f"El texto '{texto}' tiene {vocales} vocales en total")

""" 3.- Crear una función que reciba una lista de nombres y 
 muestre únicamente aquellos que tengan más de 5 letras."""

""" 4.- Crear una función que reciba una lista de notas (números decimales), 
 calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0)."""

def listaNotas(notas):
    lista = 0
    for i in range (len(notas)):
        lista += notas[i]
        if notas[i] >= 4.0 and notas[i] <= 7.0:
            print(f"El estudiante {i + 1} pasa con una nota {notas[i]}")
        elif notas[i] >= 1.0 and notas[i] <= 4.0:
            print(f"El estudiante {i + 1} no pasa con una nota {notas[i]}")
        else:
            print("Error")
        return lista / (len(notas)) + 1

def ejercicio4 ():
    largo = int(input("Cuantas notas va a ingresar: "))
    nota = []
    for i in range(largo):
        eli = float(input(f"Ingresa una nota {i+ 1}"))
        if eli != " ":
            nota.append(eli)
    print(listaNotas(nota))
    
""" 5.- Crear una función que reciba una lista de precios de productos y 
 aplique un descuento del 10%, mostrando el valor original y el nuevo valor."""

'''def aplicarDescuento(producto):
    producto = precio * cantidad
    descuento = producto * 0.1
    total = producto - descuento
    print(f"El precio inicial es: {producto}. Con descuento: {total}")

def valores():
   cantidad = int(input("Ingresa cantidad: "))
   precios = []
   for i in range(cantidad):
       precio = float(input("ingresa el precio del producto: "))
       precios.append(precio)
aplicarDescuento(precio)'''

""" 6.- Crear una función que reciba un número entero y determine si es par o impar."""

def parImpar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par.")
    elif numero % 3 == 0:
        print(f"El numero {numero} es Impar.")
    else:
        print("Error")

def recibirNum():
    num = int(input("Ingrese un numero: "))
    parImpar(num)


""" 7.- Crear una función que reciba una lista de edades y muestre cuántas 
 personas son mayores de edad (18 años o más)."""

'''def listaedades(edades):
    if edad >= 18:
        print(f"Tienes acceso ya que tu edad es: {edad} aproximadamente")
    elif edad > 0 and edad < 18:
        print(f"No tiene acceso: te faltan {18 - edad} años. ")
    else:
        print("Ingresa valores validos")

def ingresa():
    edades = []
    campo = input("Ingrese su año de nacimiento: ")
    edad = 2026 - campo
    if campo == "":
        print("Error")
    else: 
        edades.append(edad)'''

def edades(lista):
    num = 0
    for i in range(len(lista)):
        if lista[i] >= 18:
            num += 1
    return num

def personas():
    edad = []
    inp = int(input("¿Cuantas personas vas a ingresar?: "))
    for i in range (inp):
        var = int(input(">> "))
        if var != " ":
            edad.append(var)
        else:
            print("Por favor ingresar valor valido")
    resultado = edades(edad)
    print(f"Hay {resultado} personas mayores de edad")


""" 8.- Crear una función que reciba una lista de palabras y permita buscar 
 cuántas veces aparece una palabra específica ingresada por el usuario."""

""" 9.- Crear una función que reciba una lista de números y genere una nueva 
 lista que contenga únicamente los números positivos."""



""" 10.- Crear una función que reciba una lista de productos 
 (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades."""

def limpiar_consola():
    os.system('cls')

continuar = True
while continuar: 
    print("\n- Ejercicios Python -")
    print("--- Ejercicio 1 ---")
    print("--- Ejercicio 2 ---")
    print("--- Ejercicio 3 ---")
    print("--- Ejercicio 4 ---")
    print("--- Ejercicio 5 ---")
    print("--- Ejercicio 6 ---")
    print("--- Ejercicio 7 ---")
    print("--- Ejercicio 8 ---")
    print("--- Ejercicio 9 ---")
    print("--- Ejercicio 10 ---")
    opcion = input("\n---Elije una opción: (1 - 5) (0 para salir): ")
    if opcion == "1":
        limpiar_consola()
        print("\nEjecutar ejercicio 1: ")
        print(ejercicio1())
    elif opcion == "2":
        limpiar_consola()
        print("\nEjecutar ejercicio 2: ")
        eli = input("ingresa un texto: ")
        print(contadorVocales(eli))
    elif opcion == "3":
        limpiar_consola()
        print("\nEjecutar ejercicio 3: ")
        
    elif opcion == "4":
        limpiar_consola()
        print("\nEjecutar ejercicio 4: ")
        
    elif opcion == "5":
        limpiar_consola()
        print("\nEjecutar ejercicio 5: ")
    elif opcion == "6":
        limpiar_consola()
        print("\nEjecutar ejercicio 6: ")
        recibirNum()
    elif opcion == "7":
        limpiar_consola()
        print("\nEjecutar ejercicio 7: ")
        personas()
    elif opcion == "8":
        limpiar_consola()
        print("\nEjecutar ejercicio 8: ")
        
    elif opcion == "9":
        limpiar_consola()
        print("\nEjecutar ejercicio 9: ")
        
    elif opcion == "10":
        limpiar_consola()
        print("\nEjecutar ejercicio 10: ")
        
    elif opcion == "0":
        limpiar_consola()
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")