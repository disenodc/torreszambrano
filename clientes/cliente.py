class Cliente:
    tipo_cliente = "Cliente Web"  # atributo de clase

    def __init__(self, nombre, apellido, email, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.direccion = direccion
        self.compras = []

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email}"

    def agregar_compra(self, producto):
        """Agrega un producto al historial de compras."""
        self.compras.append(producto)
        print(f"{self.nombre} compró: {producto}")

    def mostrar_historial(self):
        """Muestra todos los productos comprados."""
        if not self.compras:
            print(f"{self.nombre} no tiene compras registradas.")
        else:
            print(f"Historial de compras de {self.nombre}:")
            for producto in self.compras:
                print(f"- {producto}")
