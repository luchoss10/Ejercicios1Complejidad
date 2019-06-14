# 4) Hacer una funcion que llene una matriz de
# tamaño NXM con numeros aleatorios
#
# Pre: N>=1 M>=1 Tanto N como M deben ser mayores que 0
# Post: Entrega una matriz de tamaño NxM

import random

def MNMatriz(N, M):
    
    matriz=[]
    for i in range(0, N):
        matriz.append([])
        for j in range(0, M): 
            matriz[i].append(random.randrange(99))

    return matriz

N =  int(input("Ingrese el numero de filas de la matriz: "))
M =  int(input("Ingrese el numero de columnas de la matriz: "))

if N >=1 and M>=1:
    print(str(MNMatriz(N, M)))
else:
    print("Parametros incorrectos, deben ser mayores a 0")
