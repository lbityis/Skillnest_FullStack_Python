# Creacion de la clase de usuario
class Usuario:
    def __init__(self): # 🏗️ método constructor
       self.nombre = "Nariyoshi"
       self.apellido = "Miyagi"
       self.email = "miyagi@codingdojo.la"
       self.limite_credito = 30000
       self.saldo_pagar = 0


# Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
Elisa = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) # Imprime: Nariyoshi
print(miyagi.apellido) # Imprime: Miyagi
print(miyagi.email) # Imprime: miyagi@codingdojo.la
print(miyagi.limite_credito) # Imprime: 30000
print(miyagi.saldo_pagar) # Imprime: 0

# Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 30000
print(daniel.nombre) # Imprime: Daniel

# Valores a nueva instancia
Elisa.nombre = "Elisa"
Elisa.apellido = "Soto"
Elisa.email = "elisa@gmail.com"
Elisa.limite_credito = 100000
Elisa.saldo_pagar = 2

# Imprimir nombre de cada instancia
print(miyagi.nombre) # Imprime: miyagi
print(daniel.nombre) # Imprime: Daniel
print(Elisa.nombre) # Imprime: Elisa