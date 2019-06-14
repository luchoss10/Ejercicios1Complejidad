# 1) Hacer una funcion que reciba un numero entero positivo 
# y retorne verdadero si es primo o falso si no.
# 
# Pre: Num>0 el numero debe ser mayor que 0 y entero
# Post: La funcion debe determinar si el numero es primo o no 
# devolviendo true y false respectivamente.  
#
# Complejidad = O(6) + O(2n)
# Complejidad = O(n) por teorema 2
#

def verPrim(n):
    if n<1: #O(1)
        return False # O(1)
    elif n==2: #O(1)
        return True # O(1)
    else: #O(1)
        for i in range(2, n): # O(2n)
            if n%i==0:  #O(1)
                return False #O(1)
    return True #O(1)

n = int(input("Ingrese un numero mayor a 1: "))

if n>=0:
    if verPrim(n):
        print("El numero es primo")
    else:
        print("El numero no es primo")
else:
    print("El numero es negativo")
