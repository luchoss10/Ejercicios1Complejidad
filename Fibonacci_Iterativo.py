# 6)Hacer una funcion que calcule el n-ésimo 
# número de la serie de fibonacci,
#
# Pre: n >= 0 El numero ingresado debe ser positivo o 0
# Post: Entrega el valor del n número de la serie de fibonacci
#

import sys

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        j = 0
        k = 1
        for i in range(n):
            c = k+j
            j = k
            k = c
        return j
    else:
        print("El numero introducido no es positivo")
        sys.exit(True)


print("Sucesión Fibonacci Recursiva")
num=int(input("Ingresa el numero de la serie: "))
resutado=fibonacci(num)
print("El numero de la sucesión numero " + str(num) + " de fibonacci es el : " + str(resutado))