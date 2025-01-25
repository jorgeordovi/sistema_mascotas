#funcin de interfas

from clases.inventario import Inventario
from clases.producto import Producto
from clases.cliente import Cliente
from clases.mascota import Gato, Perro
from clases.venta import Venta


def registrar_mascota():
    tipo = input("Ingrese tipo de mascota (Perro/Gato)").strip().lower()
    nombre = input("Nombre de la mascota ")
    edad = int(input("Edad de la mascota "))
    salud = input("Estado de salud de la mascota: ")
    precio = float(input("Precio de la mascota: "))

    if tipo == "perro":
        raza = input("Raza del perro: ")
        nivel_de_energia = input("Nivel de energia del Perro: ")
        mascota = Perro(nombre, edad, precio, salud, raza, nivel_de_energia)
    elif tipo == "gato":
        raza = input("Raza del gato; ")
        independencia = input("Nivel de independencia del gato: ")
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print("Tipo de mascota no roconocido")
        return

    return mascota

def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    direccion = input("Direccion del cliente: ")
    telefono = input("Telefono del cliente: ")
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

def registrar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoria del producto: ")
    precio = input("Precio del producto: ")
    cantidad = int(input("Cantidad de producto: "))
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto

def registrar_venta(clientes, inventario):
    nombre_cliente = input("Nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrados")
        return

    productos = []

    while True:
        nombre_producto = input("Nombre del producto (deja vacio para finalizar): ")
        if not nombre_producto:
            break
        producto = next((p for p in inventario.lista_de_productos if p.nombre == nombre_producto), None)
        if producto:
            productos.append(producto)
        else:
            print("Producto no encontrado")
        
    if productos:
        venta = Venta(cliente, productos)
        venta.registrar_venta()
        print("La venta ha sido registrtada con exito")
    else:
        print("No se han podido registrar la venta")

def mostrar_menu():
    print("\n --- Menu de gestion de Sistema de Mascotas ")
    print("1. Registrar Mascota")
    print("2. Registrar Cliente")
    print("3. Registrar Producto")
    print("4. Registrar Venta")
    print("5. Mostar informacion acerda de Mascotas")
    print("6. Mostar informacion acerda de Clientes")
    print("7. Mostar informacion acerda de Productos")
    print("8. Generar lista de inventario")
    print("9. Salir")
    
def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una Opcion: ")

        if opcion == "1":
            mascota = registrar_mascota()
            if mascota:
                mascotas.append(mascota)
                print("mascota registrtada con exito")
        
        elif opcion == "2":
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print("Cliente registrado con exito")
        
        elif opcion == "3":
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)#///
                print("Producto registrado con exito")
            
        elif opcion == "4":
            registrar_venta(clientes, inventario)
        elif opcion == "5":
            for mascotas in mascotas:
                print(mascotas.mostrar_informacion())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrar_caracteristicas())
        elif opcion == "6":
            for cliente in clientes:
                print(cliente.mostrar_informacion())
        elif opcion == "7":
            for producto in inventario.lista_de_productos:
                print(producto.mostrar_informacion())
        elif opcion == "8":
            umbral_mininmo = int(input("Ingrese el umbreal minimo del inventario: "))
            print(inventario.generar_alerta(umbral_mininmo))
        elif opcion == "9":
            print("Saliendo del sistetma. Gracias por usar Sistema de mascotas")
            break
        else:
            print("Opcion no valida, vuelva a intentar")

if __name__ == "__main__":
    main()