''' Guía de Ejercicios: Lógica Fundamental '''

# I. Interacción y Condicionales (Básico)
"""1. Números Pares Dinámicos
Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). 
El programa debe imprimir los primeros $n$ números pares positivos.
"""
def numerosDinamicos():
    num = int(input("¿Cuantos números desea ver?: "))
    pares = []
    for i in range(1,(num * 2) + 1):
        if i % 2 == 0:
            pares.append(i)
    print(f"Mostrando pares: {pares}")

""" 2. Verificador de Edad y Acceso
Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). 
Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
- anio = int(input("Ingrese su año de nacimiento: "))
edad = 2026 - anio
if edad >= 18:
    print("Eres mayor de edad.")
else:
    faltan = 18 - edad
    print(f"Eres menor de edad. \nTe faltan {faltan} años para ser mayor de edad.")"""

def verificador_edad():
    campo = input("Ingrese su año de nacimiento: ")
    edad = 2026 - int(campo)
    if campo == "":
        print("Error")
    elif edad >= 18:
        print(f"Tienes acceso ya que tu edad es: {edad} aproximadamente")
    elif edad > 0 and edad < 18:
        print(f"No tiene acceso: te faltan {18 - edad} años. ")
    else:
        print("Ingresa valores validos")

""" 3. Calculadora de Descuentos
Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, aplica un 15% de descuento. 
Muestra el subtotal, el descuento aplicado y el total final."""

def aplicarDescuento():
    precio = float(input("ingresa el precio del producto: "))
    cantidad = int(input("Ingresa cantidad: "))
    producto = precio * cantidad
    if producto >= 100:
        descuento = producto * 0.15
    else:
        descuento = 0
    total = producto - descuento
    print(f"El subtotal es: {producto}. El descuento aplicado es: {descuento}. El total es {total}.")


"""4. Clasificador de Números
Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, 
Negativo-Par, Negativo-Impar o Cero."""

def clasificadorNum():
    num = int(input("Ingrese in numero: "))
    if num > 0:
        if num % 2 == 0:
            print("Positivo - Par")
        elif num % 2 == 1:
            print("Positivo - Impar")
    elif num < 0: 
        if num % 2 == 0:
            print("Negativo - Par")
        elif num % 2 == 1:
            print("Negativo - Impar")
    else:
        print("Es 0")

# II. Iteraciones y Bucles (Intermedio)
""" 5. Tabla de Multiplicar Personalizada
Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, 
pero solo muestra los resultados que sean múltiplos de 3.
"""

def tablaMultiplicar():
    num = int(input("Ingresar numero a trabajar: "))
    for i in range (1, 13):
        resultado = num * 1
        if resultado % 3 == 0:
            print(f"De {num} solo estos numeros son divisibles por 3 : {resultado}")

""" 6. Sumatoria con Centinela
Crea un programa que pida números continuamente y los sume. 
El ciclo debe terminar cuando el usuario ingrese un número negativo. 
Al final, muestra la suma total (sin incluir el negativo).
"""

def sumatoriaCentinela ():
    total = 0
    while True:
        num = int(input("Ingresa un numero: "))
        if num < 0:
            break
        total += num
    print(f"Suma total de los numeros: {total}")

"""7. Contador de Vocales
Pide al usuario una frase o palabra. Utiliza un bucle para recorrer 
la cadena y contar cuántas vocales tiene en total.
"""

def contadorVocales():
    texto = input("Ingresa una palabra o frase: ").lower()
    vocales = 0
    for i in range(len(texto)):
        if texto[i] == "a" or texto[i] == "e" or texto[i] == "i" or texto[i] == "o" or texto[i] == "u" :
            vocales += 1
    print(f"La/s palabra/s {texto} tiene {vocales} vocales en total")

"""8. Validación de Contraseña
Define una contraseña en una variable. Pide al usuario que la intente adivinar. 
Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.
"""
def validacionContraseña():
    contraseña = "ELIIII"
    maxIntento = 3
    for i in range(maxIntento):
        intento = input(f"Adivina la contraseña: ")
        if intento == contraseña:
            print("¡Buen trabajo!")
            return 
        if i < maxIntento - 1:
            print("Intenta de nuevo.")
    print("Acceso bloqueado.")


# III. Manejo de Arreglos / Listas (Avanzado)

"""9. Registro de Nombres
Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. 
Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.
"""

def registroNombres():
    registro = []
    for i in range(5):
        nombre = input(f"Ingresar nombre: ")
        registro.append(nombre)
    registro.reverse()
    print(f"Registro de nombres en orden inverso: {registro}")


"""10. Promedio de Notas
Solicita al usuario cuántas notas desea ingresar. 
Almacena cada nota en un arreglo. Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.
"""

def promedioNota():
    cantidad = int(input("¿Cuantas notas desea ingresar? :"))
    notas = []
    for i in range(cantidad):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)
    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio}")
    print(f"Nota mas alta: {max(notas)}")
    print(f"Nota mas baja: {min(notas)}")

"""11. Filtro de Arreglos
Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga 
solo los números que sean mayores a 50. Muestra ambos arreglos.
"""

def filtroArreglo():
    cantidad = int(input("¿Cuantos numeros desea ingresar? :"))
    usuario = []
    mayor50 = []
    for i in range(cantidad):
        dato = int(input("Ingresar dato: "))
        usuario.append(dato)
        if dato > 50:
            mayor50.append(dato)
    print(f"Arreglo usuario: {usuario}")
    print(f"Arreglo solo con numeros mayores a 50: {mayor50} ")


"""12. Buscador de Elementos
Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y 
el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está."""

def buscadorCiudad():
    ciudades = ["Santiago", "Paris", "Londres", "Lima", "Berlin", "Buenos Aires", "Rio", "Tokio", "Caracas", "Seoul"]
    ciudad = input("Ingresar ciudad").capitalize()
    esta = ciudades.index(ciudad)
    if esta < len(ciudades):
        print(f"Tu ciudad está en el arreglo, en la posición {esta}")
    else:
        print("Tu ciudad no está en el arreglo")

# IV. Retos de Lógica Combinada


""" 13. Simulación de Inventario
Crea dos arreglos: uno para nombres_productos y otro para precios. 
Permite al usuario ingresar 3 productos con sus precios. Luego, 
muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].
"""
def simulacionInventario():
    nombres_producto = []
    precios = []

"""14. Generador de Lista de Compras
Usa un bucle while para que el usuario agregue artículos a una lista de compras. 
El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.
"""
def listaCompra():
    lista = []
    while True:
        item = input("Articulo (o 'terminar')")
        if item.lower() == "terminar":
            break
        lista.append(item)
    print(f"Ordenada: {sorted(lista)}")

"""15. Análisis de Temperaturas
Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
El promedio semanal.
Cuántos días la temperatura fue superior a 25 grados.
El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).
"""
def analisisTemperatura():
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    diasSuperior = []
    total = 0
    baja = 100
    diaBaja = ""
    cant = 0
    while cant < 7:
        temps = float(input(f"Ingrese temperatura del dia {dias[cant]}: "))
        total += temps
        if temps < baja and temps <25:
            baja = temps
            diaBaja = dias[cant]
        elif temps > 25:
            diasSuperior.append(dias[cant])
        cant += 1
    print(f"El promedio de las temperaturas fue de {total / 7}")
    print(f"El dia con la temperatura mas baja fue el dia {diaBaja} con {baja}")
    print(f"Los dias mas calurosos fueron: {diasSuperior}")

# Menu de navegacion para ejercicios
continuar = True
while continuar:
    print("\n---Ejercicios Python---")
    print("--- 1.- Ejercicio 1 ---")
    print("--- 2.- Ejercicio 2 ---")
    print("--- 3.- Ejercicio 3 ---")
    print("--- 4.- Ejercicio 4 ---")
    print("--- 5.- Ejercicio 5 ---")
    print("--- 6.- Ejercicio 6 ---")
    print("--- 7.- Ejercicio 7 ---")
    print("--- 8.- Ejercicio 8 ---")
    print("--- 9.- Ejercicio 9 ---")
    print("--- 10.- Ejercicio 10 ---")
    print("--- 11.- Ejercicio 11 ---")
    print("--- 12.- Ejercicio 12 ---")
    print("--- 13.- Ejercicio 13 ---")
    print("--- 14.- Ejercicio 14 ---")
    print("--- 15.- Ejercicio 15 ---")

    opcion = input("\n----Elige una opcion: (1-15) (0para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        print(numerosDinamicos())
    elif opcion == "2":
        print("\nEjecutando ejercicio 2: ")
        print(verificador_edad())
    elif opcion == "3":
        print("\nEjecutando ejercicio 3: ")
        print(aplicarDescuento())
    elif opcion == "4":
        print("\nEjecutando ejercicio 4: ")
        print(clasificadorNum())
    elif opcion == "5":
        print("\nEjecutando ejercicio 5: ")
        print(tablaMultiplicar())
    elif opcion == "6":
        print("\nEjecutando ejercicio 6: ")
        print(sumatoriaCentinela())
    elif opcion == "7":
        print("\nEjecutando ejercicio 7: ")
        print(contadorVocales())
    elif opcion == "8":
        print("\nEjecutando ejercicio 8: ")
        print(validacionContraseña())
    elif opcion == "9":
        print("\nEjecutando ejercicio 9: ")
        print(registroNombres())
    elif opcion == "10":
        print("\nEjecutando ejercicio 10: ")
        print(promedioNota())
    elif opcion == "11":
        print("\nEjecutando ejercicio 11: ")
        print(filtroArreglo())
    elif opcion == "12":
        print("\nEjecutando ejercicio 12: ")
        print(buscadorCiudad())
    elif opcion == "13":
        print("\nEjecutando ejercicio 13: ")
        print(simulacionInventario())
    elif opcion == "14":
        print("\nEjecutando ejercicio 14: ")
        print(listaCompra())
    elif opcion == "15":
        print("\nEjecutando ejercicio 15: ")
        print(analisisTemperatura())
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no valida, intenta otra vez")