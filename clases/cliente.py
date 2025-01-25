class Cliente  :
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial_de_compras = []

    def actualizar_informacion(self, direccion=None, telefono=None):
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono

    def registrar_compra(self, comprar):
        self.historial_de_compras.append(comprar)

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre}, Direccion: {self.direccion}, Telefono: {self.telefono}"
        