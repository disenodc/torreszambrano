import json
from clientes.cliente import Cliente
from clientes.cliente_premium import ClientePremium

class GestorClientes:
    def __init__(self, archivo_clientes="clientes.json"):
        self.clientes = []
        self.archivo_clientes = archivo_clientes
        self.cargar_clientes()

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente registrado: {cliente}")
        self.guardar_clientes()

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            print("Lista de clientes:")
            for c in self.clientes:
                print(f"- {c}")

    def guardar_clientes(self):
        datos = []
        for c in self.clientes:
            datos.append({
                "nombre": c.nombre,
                "apellido": c.apellido,
                "email": c.email,
                "direccion": c.direccion,
                "tipo": c.tipo_cliente,
                "compras": c.compras
            })
        with open(self.archivo_clientes, "w") as f:
            json.dump(datos, f, indent=4)

    def cargar_clientes(self):
        try:
            with open(self.archivo_clientes, "r") as f:
                datos = json.load(f)
            for c in datos:
                if c["tipo"] == "Cliente Premium":
                    nuevo = ClientePremium(c["nombre"], c["apellido"], c["email"], c["direccion"])
                else:
                    nuevo = Cliente(c["nombre"], c["apellido"], c["email"], c["direccion"])
                nuevo.compras = c["compras"]
                self.clientes.append(nuevo)
        except FileNotFoundError:
            pass
