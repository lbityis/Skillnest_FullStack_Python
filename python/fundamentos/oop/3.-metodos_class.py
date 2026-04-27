class Usuario:
   def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0

   def hacer_compra(self, monto): # recibe como argumento el monto de la compra
       self.saldo_pagar += monto # el saldo a pagar del usuario aumenta en la cantidad del valor recibido

   def aumentarCredito(self, aumento):
       self.limite_credito += aumento

   def cambiaremail(self, nuevoemail):
       self.email = nuevoemail

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

# Compras miyagi
print(f"--- Compras de {miyagi.nombre}: ---")
miyagi.hacer_compra(2000)
print(f"Primera compra: ${miyagi.saldo_pagar}")
segundacompra = 300
miyagi.hacer_compra(segundacompra)
print(f"Segunda compra: ${segundacompra}")
print(f"Total compra: {miyagi.saldo_pagar}") #Imprime: 350
# Imprimir cuanto credito le queda a Miyagi
print(f"Credito disponible de {miyagi.nombre}: ${miyagi.limite_credito - miyagi.saldo_pagar}")

# Compras Daniel
print(f"--- Compras de {daniel.nombre}: ---")
daniel.hacer_compra(45)
print(f"Primera compra: {daniel.saldo_pagar}") #Imprime: 45
print(f"Total compra: {daniel.saldo_pagar}") #Imprime: 350
# Imprimir cuanto credito le queda a Miyagi
print(f"Credito disponible de {daniel.nombre}: ${daniel.limite_credito - daniel.saldo_pagar}")

####### ACTIVIDAD #######

'''1.- Crear un nuevo metodo que permita aumentar el limite de credito.
   Imprimir el nuevo limite de credito.'''

daniel.aumentarCredito(5000)
print(f"El nuevo limite de credito de {daniel.nombre} es de {daniel.limite_credito}")

'''2.- Crear un metodo que permita cambiar el correo de la instancia.'''

miyagi.cambiaremail("mimi@gmail.com")
print(f"Nuevo email de {miyagi.nombre}: {miyagi.email}")