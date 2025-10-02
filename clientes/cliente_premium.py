from clientes.cliente import Cliente

class ClientePremium(Cliente):
    tipo_cliente = "Cliente Premium"

    def __init__(self, nombre, apellido, email, direccion, descuento=10):
        super().__init__(nombre, apellido, email, direccion)
        self.descuento = descuento  # descuento en %

    def aplicar_descuento(self, precio):
        """Devuelve el precio con descuento aplicado."""
        return precio * (1 - self.descuento / 100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} (Premium) - {self.email}"
