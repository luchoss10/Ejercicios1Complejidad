# 3)Hacer una función que llene un vector 
# (de tamaño N) con números enteros aleatorios (puede ser de 4 cifras)
#
#   Pre: N>=1 El tamaño del vector esta dado po N y deve ser mayor o igual 1
#   Post: Entrega el vector de tamaño N con los datos aleatorios

import random

def NVector(n):
    lista = []
    for i in range(0, n):
        lista.append(random.randrange(9999))
    return lista

N =  int(input("Ingrese un tamaño para el vector: "))

if N>=1:
    print("El vector es: " + str(NVector(N)))
else:
    print("No pueden existir Vectores de tamaño menor que 1")
