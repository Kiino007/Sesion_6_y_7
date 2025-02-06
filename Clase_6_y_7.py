# Sesion 6 y 7:  Tipos de funciones, parametros y referencias
#Objetivos:

#1. comprender los diferentes tipos de funciones y sus parametros

#2. Aplicar funciones con parametros y valores de retorno en problemas complejos

#3. Implementar busquedas y ordenaciones dentro de listas y matrices

#4. Resolver problemas con programacion modular 

#Retorno y parametros
#Las funciones pueden recibir datos de entrada que son parametros, y devolver valores procesados que serian los retornos
#Crear una funcion que reciba una lista de ventas mensuales y calcule el total venidod el mes con mayores ventas y el 
#mes con menores ventas

def analizar_ventas(ventas):
    total = sum(ventas)
    max_venta = max(ventas)
    min_venta = min(ventas)

    return total, ventas.index(max_venta), ventas.index(min_venta)

#datos de ventas mensuales (ene, feb, marz, abr, etc...)
    
ventas_mensuales = [1500, 3200, 1800, 4000, 2100, 3500, 3900, 2800, 4700, 2600, 3000, 4200]

total, mes_max, mes_min = analizar_ventas(ventas_mensuales)

print(f"Total vendido en el año fue {total}")
print(f"El mes con mayores ventas fue el numero {mes_max+1} con $ {ventas_mensuales[mes_max]}") 
print(f"El mes con menores pentas fue el numero {mes_min+1} con $ {ventas_mensuales[mes_min]}")
