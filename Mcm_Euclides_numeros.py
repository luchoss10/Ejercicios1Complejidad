# 7)Hacer una función que retorne el mcm(mínimo común múltiplo)
# de 2 números naturales mayores que 0 por el metodo de Euclides
#
# Pre: n y m > 0 los numeros introducidos deben ser mayores que 0
# Post: Entrega el mcm de ambos numeros
#
# Complejidad =  O(11) + O(6n)
# Complejidad = O(6n) por teorema 2, sin embargo el comportamiento 
# matematico de la ecuacion es logaritmico debido al numero y metodo 
# de iteración para encontrar el MCD, que es que n.
#

import sys

def McmEucl(n1, n2):

    if n1 > 0  and n2>0: #O(1)
        if n1>n2: #O(1)
            m = n1 #O(1)
            n = n2 #O(1)
        else: #O(1)
            m = n2 #O(1)
            n = n1 #O(1)
        while True: #O(6n)
            res = m % n #O(1)
            if res == 0: #O(1)
                mcd = n #O(1)
                break #O(1)
            m = n #O(1)
            n = res #O(1)
        
        return (n1*n2)/mcd #O(1)
    else: #O(1)
        print("Alguno de los númeroses menor que 0") #O(1)
        sys.exit(True) #O(1)



num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))

print("El Minimo Comun Multiplo de los numeros es: " + str(McmEucl(num1, num2)))