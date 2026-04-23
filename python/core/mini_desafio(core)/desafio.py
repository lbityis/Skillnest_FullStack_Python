# 🎯 MINI DESAFÍO (nivel core)

datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]

# 1. Cambiar el puntaje de Pedro a 75
datos[2]["puntaje"] = 75
print(datos)

# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
def carlos(e): 
   print(f"{datos[0]["nombre"]} obtuvo {datos[0]["puntaje"]} puntos")
carlos(datos)

# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores
def recibe(clave, lista):
   for a in range(len(lista)):
      if lista[a] in lista:
         print(lista[a][clave]) 
recibe("nombre", datos)
recibe("puntaje", datos)
