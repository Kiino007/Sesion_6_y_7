#Ordenamiento avanzado de listas

#Recibir una lista de estudiantes con sus calificaciones y ordenarla de mayor a menor (timsort)

def ordenar_estudiantes(estudiantes):
    estudiantes.sort(key = lambda x: x[1], reverse = True)

estudiantes= [
    ("juan", 85),
    ("maria", 92),
    ("carlos", 78),
    ("ana", 95),
    ("pedro", 88)
]

ordenar_estudiantes(estudiantes)

print("Lista de estudiantes ordenada por nota final")
for estudiante in estudiantes:
    print(f"{estudiante[0]} - nota: {estudiante[1]}")