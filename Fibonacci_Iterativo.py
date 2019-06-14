# 6)Hacer una funcion que calcule el n-ésimo 
# número de la serie de fibonacci,
#
# Pre: n >= 0 El numero ingresado debe ser positivo o 0
# Post: Entrega el valor del n número de la serie de fibonacci
#
# Complejidad =  O(9) + O(3n)
# Complejidad = O(n) por teorema 2
#

import sys

def fibonacci(n): 
    if n == 0 or n == 1: #O(1)
        return 1 #O(1)
    elif n > 1: #O(1)
        j = 0 #O(1)
        k = 1 #O(1)
        for i in range(n): #O(3n)
            c = k+j #O(1)
            j = k #O(1)
            k = c #O(1)
        return j #O(1)
    else: #O(1)
        print("El numero introducido no es positivo") #O(1)
        sys.exit(True) #O(1)


print("Sucesión Fibonacci Recursiva")
num=int(input("Ingresa el numero de la serie: "))
resutado=fibonacci(num)
print("El numero de la sucesión numero " + str(num) + " de fibonacci es el : " + str(resutado))