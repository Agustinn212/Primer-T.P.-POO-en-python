# main.py
from electronico import Electronico
from alimento import Alimento

# Crear una instancia de Electronico
telefono = Electronico(nombre="Teléfono Inteligente", precio=999.99, cantidad=10, marca="Apple", modelo="Iphone 15 pro")
# Crear una instancia de Alimento
manzanas = Alimento(nombre="Manzanas", precio=3.99, cantidad=50, fecha_expiracion="2024-12-31")

# Mostrar la información de cada producto
print(telefono.mostrar_informacion())
print(manzanas.mostrar_informacion())

