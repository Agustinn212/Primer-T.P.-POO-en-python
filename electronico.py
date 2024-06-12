# electronico.py
from producto import Producto

class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, marca, modelo):
        """
        Inicializa un nuevo producto electrónico con nombre, precio, cantidad, marca y modelo.
        
        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        :param cantidad: Cantidad disponible del producto.
        :param marca: Marca del producto electrónico.
        :param modelo: Modelo del producto electrónico.
        """
        Producto.__init__(self, nombre, precio, cantidad)
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        """
        Muestra la información completa del producto electrónico.
        
        :return: Información del producto electrónico en formato string.
        """
        info_basica = Producto.mostrar_informacion(self)
        return f"{info_basica}, Marca: {self.marca}, Modelo: {self.modelo}"
