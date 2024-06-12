# producto.py
class Producto:
    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa un nuevo producto con nombre, precio y cantidad.
        
        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        :param cantidad: Cantidad disponible del producto.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        """
        Muestra la información del producto.
        
        :return: Información del producto en formato string.
        """
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"
