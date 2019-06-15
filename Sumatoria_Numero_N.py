# 2) Hacer una función que reciba un valor N 
# y retorne la sumatoria de los eneros hasta N 
#
# Pre: N>=1 El número N debe ser mayor que 1 para empezar la sumatoria
# Post: Se debe entregar la suma de todos los numeros hasta el numero N
#
# Complejidad = O(5) + O(n)
# Complejidad = O(n) por teorema 2
# Complejidad Sumatoria por formula = O(1)
#

def sumatoria(n):
    if n >=1: #O(1)
        j = 0 # O(1)
        for i in range(0, n): # O(n)
           j = i+j #O(1) 
        return j # O(1)
    else: #O(1)
        return "El numero es negativo" #O(1)

def SumatoriaFomula(n):
    if n>= 1: #O(!)
        return (n*(n+1))/2 #O(1)
    else:
        return "El numero es negativo" #O(1)
    
num = int(input("Ingrese un numero para sumatoria: "))

print(str(sumatoria(num)))



