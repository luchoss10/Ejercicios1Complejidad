# 5) Hacer una funcion que reciba 2 matrices de tamaño NxM
# y MxP respectivamente y devuelva otra matriz con la multiplicacion
# de las dos primeras.
#
# Pre: N, M, P>=1 Los valores introducidos deben ser maores a 0
# Post: Entrega la multiplicaicon de las matrices formadas
#
# Complejidad =  O(2) + O(n) + O(n^3)
# Complejidad = O(n^3) por teorema 2
#

import random

def BuildMatriz(N, M):

    matriz=[] 
    for i in range(0, N): 
        matriz.append([]) 
        for j in range(0, M): 
            matriz[i].append(random.randrange(10)) 
    return matriz 

def MultMatrices(m1, m2):
    resultado = [] #O(1)
    for i in range(len(m1)): #O(n)
        resultado.append([0] * len(m2[0])) #O(1)
    
    for i in range(len(m1)): #O(n)
        for j in range(len(m2[0])): #O(n)
            for k in range(len(m1[0])): #O(n) =O(n) * O(n) * O(n) por teorema 3
                resultado[i][j] += m1[i][k] * m2[k][j] #O(1)

    return resultado #O(1)
         
N = int(input("Ingrese el valor de filas de la matriz 1: ")) 
M = int(input("Ingrese el valor de columnas de la matriz 1 y filas de la matriz 2: "))
P = int(input("Ingrese el valor de columnas de matriz 2: "))

if N > 0 and M > 0 and P > 0:
    matriz1 = BuildMatriz(N, M)
    matriz2 = BuildMatriz(M, P)
    matrizResultado = MultMatrices(matriz1, matriz2)
    print(str(matriz1))
    print(str(matriz2))
    print(str(matrizResultado))
else:
    print("Parametros incorrectos, deben ser mayores a 0")