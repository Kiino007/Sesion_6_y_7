#Funcion con paso por referencia(listamutable)
#cuando una funcion recibe una lista como parametro, puede modificarla directamente

#Ejemplo 2:
#Crear una funcion que reciba un inventario de productos y permita actualizar cantidades segun las compras

def actualizar_inventario(inventario, producto, cantidad_comprada):
    if producto in inventario:
        inventario[producto] -= cantidad_comprada
        if inventario[producto] < 0:
            inventario[producto] = 0

        else:
            print(f"producto no encontrado en el inventario")

#inventario de prueba
inventario = {
    "laptop" : 10,
    "mouse" : 25,
    "teclado" : 15,
    "monitor" : 8
}

producto_solicitado = input("Ingrese el producto comprado: ")
cantidad = int(input(f"Ingrese la cantidad de {producto_solicitado} comprada"))

actualizar_inventario(inventario, producto_solicitado, cantidad)

print("inventario actualizado: ", inventario)