#Funciones en Python
def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
   resultado = num1 * num2     #instrucciones dentro de la función
   return resultado            #regresamos valor de resultado
a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))
resultado_multiplicacion = multiplicacion(a, b) #Llamado a la función con argumentos 5 y 5
print(resultado_multiplicacion) #Se guarda en la variable el resultado que la función regresó. Imprime: 25


# Parámetros y argumentos
def buenos_dias(nombre):
   print("Buenos días "+nombre)
# Una vez definida la función, podemos invocarla llamándola por su nombre y enviando la cantidad de argumentos requeridos:
buenos_dias("alegría")
buenos_dias("al amor")
buenos_dias("a la vida")
buenos_dias("señor Sol")


# Devolución de valores
def buenos_dias2(nombre):
   return "Buenos días "+nombre
frase = buenos_dias2("Python") #El valor de retorno de la función es "Buenos días Python", por lo que el valor de mi variable frase será ese
print(frase) #Imprime: Buenos días Python


# Ejercicio de retorno de valor.
# Crear una funcion que reciba dos parametros (una frase y una palabra)
# Devolver el valor de la frase completa e imprimir
def crearfrase(frase, palabra):
   return f"{frase} {palabra}"
frase = input("Ingrese una frase: ")
palabra = input("Ingrese una palabra: ")
resultadoFrase = crearfrase(frase, palabra)
print(resultadoFrase)