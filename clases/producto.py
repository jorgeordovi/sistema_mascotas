class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantididad = cantidad

    def actualizar_cantidad(self, cantidad):
        self.cantididad = cantidad
    
    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, Catetgoria: {self.categoria}, Precio: {self.precio}, Cantitdad: {self.cantididad}"