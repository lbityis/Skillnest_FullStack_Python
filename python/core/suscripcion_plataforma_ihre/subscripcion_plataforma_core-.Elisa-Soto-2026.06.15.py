class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        if tipo_suscripcion in self.costos_suscripcion:
            self.tipo_suscripcion = tipo_suscripcion
        else:
            self.tipo_suscripcion = "Gratis"
            
        self.costo_mensual = self.costos_suscripcion[self.tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        self.saldo_pendiente -= monto
        print(f"Pago registrado: {self.usuario} abonó {monto}. Saldo pendiente: {round(self.saldo_pendiente, 2)}")

    def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in self.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
            self.saldo_pendiente += self.costo_mensual
            print(f"Actualización: {self.usuario} cambió a plan {nuevo_tipo}")
        else:
            print(f"Error: El tipo de suscripción '{nuevo_tipo}' no es válido")

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Gratis":
            print(f"Acceso denegado: El usuario {self.usuario} requiere un plan superior")
        else:
            print(f"Acceso concedido: {self.usuario} está viendo contenido exclusivo")

    def mostrar_info_suscripcion(self):
        print("-" * 20)
        print(f"Usuario: {self.usuario}")
        print(f"Tipo: {self.tipo_suscripcion}")
        print(f"Cuota mensual: {self.costo_mensual}")
        print(f"Deuda actual: {round(self.saldo_pendiente, 2)}")
        print("-" * 20)

# Pruebas de ejecución
if __name__ == "__main__":
    # Instancias iniciales
    u1 = SuscripcionStreaming("Ana", "Gratis")
    u2 = SuscripcionStreaming("Beto", "Estándar")
    u3 = SuscripcionStreaming("Carla", "Premium")

    # Usuario 1
    u1.ver_contenido_exclusivo()
    u1.cambiar_suscripcion("Estándar")
    u1.realizar_pago(5.99)
    u1.mostrar_info_suscripcion()

    # Usuario 2
    u2.ver_contenido_exclusivo()
    u2.cambiar_suscripcion("Premium")
    u2.realizar_pago(5.00)
    u2.realizar_pago(11.98)
    u2.mostrar_info_suscripcion()

    # Usuario 3
    u3.realizar_pago(5.00)
    u3.ver_contenido_exclusivo()
    u3.mostrar_info_suscripcion()