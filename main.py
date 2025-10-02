from clientes.cliente import Cliente
from clientes.cliente_premium import ClientePremium
from clientes.gestor_clientes import GestorClientes

# Crear el gestor (carga clientes si existe el archivo)
gestor = GestorClientes()

# Crear clientes y registrarlos
c1 = Cliente("Ana", "Martínez", "ana@email.com", "Av. Siempre Viva 742")
c2 = ClientePremium("Luis", "Gómez", "luis@email.com", "Calle Falsa 123", descuento=15)

gestor.registrar_cliente(c1)
gestor.registrar_cliente(c2)

# Agregar compras
c1.agregar_compra("Notebook HP")
c1.agregar_compra("Auriculares Logitech")
c2.agregar_compra("Mouse Gamer")

# Mostrar historial
c1.mostrar_historial()
c2.mostrar_historial()

# Ejemplo de uso de descuento premium
precio_original = 1000
precio_con_descuento = c2.aplicar_descuento(precio_original)
print(f"Precio original: ${precio_original} - Con descuento: ${precio_con_descuento}")

# Listar todos los clientes
gestor.listar_clientes()
