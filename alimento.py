# alimento.py
from producto import Producto

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        """
        Inicializa un nuevo producto alimenticio con nombre, precio, cantidad y fecha de expiración.
        
        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        :param cantidad: Cantidad disponible del producto.
        :param fecha_expiracion: Fecha de expiración del producto alimenticio.
        """
        Producto.__init__(self, nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion

    def mostrar_informacion(self):
        """
        Muestra la información completa del producto alimenticio.
        
        :return: Información del producto alimenticio en formato string.
        """
        info_basica = Producto.mostrar_informacion(self)
        return f"{info_basica}, Fecha de Expiración: {self.fecha_expiracion}"
