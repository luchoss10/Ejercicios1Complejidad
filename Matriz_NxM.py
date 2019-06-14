# 4) Hacer una funcion que llene una matriz de
# tamaño NXM con numeros aleatorios
#
# Pre: N>=1 M>=1 Tanto N como M deben ser mayores que 0
# Post: Entrega una matriz de tamaño NxM
#
# Complejidad =  O(2) + O(n) + O(n^2)
# Complejidad = O(n^2) por teorema 2
#

import random 

def MNMatriz(N, M):
    matriz=[] # O(1)

    for i in range(0, N): # O(n)
       matriz.append([0] * M) #O(1)

    for i in range(0, N): #O(n) 
        for j in range(0, M): #O(n) = O(n) * O(n) por teorema 3
            matriz[i][j] = random.randrange(99) #O(1)
    return matriz #O(1)

N =  int(input("Ingrese el numero de filas de la matriz: "))
M =  int(input("Ingrese el numero de columnas de la matriz: "))

if N >=1 and M>=1:
    print(str(MNMatriz(N, M)))
else:
    print("No pueden existir ")
