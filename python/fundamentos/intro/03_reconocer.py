## Este archivo demuestra varios conceptos básicos en Python.
# Completa los comentarios en cada línea para relacionarlos
# con los conceptos enumerados en 'reconocer.md'.


import random # Importacion de libreria para procesos aleatoreos

nombre = "Frida Kahlo" # Creacionde variable tipo string y se asigna unvalor 
print(type(nombre)) # type() = Metodo de python para mostrar el tipo de una variable
print(len(nombre)) # len() = Devuelve ellargo de una variable 

edad = 25 # Creacion de variable tipo numerico(int)

if edad < 18: # Se establece condicion if 
   print("Eres menor de edad.") # Imprime un mesaje
elif edad == 18: # Se establece subcondicion elif(else if)
   print("Tienes 18 años.") # Imprime un mensaje
else: # Cierre de condicion (si no se cumplen condiciones anteriores)
   print("Eres mayor de edad.") # Imprime un mensaje

frutas = ["manzana", "pera", "fresa"] # Creacion de arreglo(array) con valores ya asignados
print(frutas[0]) # Mostramos la primera posicion del arreglo
frutas[0] = "banana" # A la posicion 0 del arreglo se le asigna el valor de "Banana"
frutas.append("uva") # Se le agrega "uva" al final del arreglo
frutas.remove("pera") # Se remueve la palabra "pera" del arreglo

dimensiones = (200, 50) # Creamos una variable tipo tupla (variable inmutable)
print(dimensiones[0]) # Imprime la posicion 0 de la variable creada 

persona = { # Variable tipo object
   "nombre": "Carlos", # Se establece un item y su respectivo valor
   "edad": 30 # Se establece un item y su respectivo valor
}
print(persona["nombre"]) # Imprime el valor del item (ej: "Carlos")
persona["edad"] = 31 # Se modifica el valor del item edad a 31
persona["ciudad"] = "Santiago" # Se agrega un nuevo item con un valor
del persona["ciudad"] # Se elimina el item completo

for i in range(5): # for range: Se crea bucle en rango desde 0 a 5
   if i == 2: # Se establece condicion if == 2
       continue # continue : Ignora el proceso y continua
   if i == 4: # Se establece condicion if == 4
       break # Si i = 4 se rompe el bucle
   print(i) # Imprime el valor de i en cada interacion (hasta 4)

contador = 0 # Se crea una variable contador tipo numerico(int)
while contador < 3: # Se crea bucle while con una condicion
   print(f"while contador es: {contador}") # Imprime el contador en un mensaje concatenado con f"" string
   contador += 1 # Incrementa el valor en 1 en cada iteracion

def saludar_usuario(nombre): # def - Palabra reservada para crear una funcion
   return f"Hola, {nombre}" # Devuelve un valor de la funcion

print(saludar_usuario("Francisca")) # Se imprime "Hola Francisca" - return de la funcion