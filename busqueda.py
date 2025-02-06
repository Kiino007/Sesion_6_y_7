#Busqueda avanzada en una matriz
#localizacion de un producto en una tienda

#dada la matriz que represente los estantes de una tienda, buscar un producto y devolcer su ubicacion

def buscar_producto(matriz, producto):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == producto:
                return i,j
    return None

tienda = [
    ["laptop", "teclado", "mouse"],
    ["monitor", "procesador", "parlantes"],
    ["impresora", "webcam", "router"]
]

producto_buscar = input("ingrese el nombre del producto que quieres buscar: ")
ubicacion = buscar_producto(tienda, producto_buscar)

if ubicacion:
    print(f"El producto '{producto_buscar}' esta en la fila {ubicacion[0]} y columna {ubicacion[1]}.")
else:
    print(f"El producto '{producto_buscar}' no esta en la tienda.")