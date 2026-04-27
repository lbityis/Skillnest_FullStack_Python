# ➡️ Pasar argumentos 
'''Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al método __init__
 y que de esta manera podamos asignarle a los atributos los valores correspondientes.'''

class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar

# Creacion de las instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 30000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 50000, 1000)
eli = Usuario("Elisa", "Soto", "elisa@gmail.com", 56000, 20)

# Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

###############################################################################################

# Tarea rápida : 
'''Crear una clase estudiante y asignarle los siguientes 
 atributos = rut, nombre,apellido, especialidad, fecha_nac.
 Crear 3 instancias para la clase con distintos estudiantes.
 Imprimir el nombre y apellido concatenado + especialidad.'''

class Estudiante:
   def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
       self.rut = rut
       self.nombre = nombre
       self.apellido = apellido
       self.especialidad = especialidad
       self.fecha_nac = fecha_nac

sergio = Estudiante(227563324,"Sergio", "Bustos", "programacion", 28/6/2008)
martin = Estudiante(228406325,"Martin", "Rojas", "programacion", 4/10/2008)
eli = Estudiante(228811734,"Elisa", "Soto", "programacion", 25/11/2008)

print(sergio.nombre + " " + sergio.apellido + " " + sergio.especialidad)
print(martin.nombre + " " + martin.apellido + " " + martin.especialidad)
print(eli.nombre + " " + eli.apellido + " " + eli.especialidad)
      