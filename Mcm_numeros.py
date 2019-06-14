# 7)Hacer una función que retorne el mcm(mínimo común múltiplo)
# de 2 números naturales mayores que 0
#
# Pre: n y m > 0 los numeros introducidos deben ser mayores que 0
# Post: Entrega el mcm de ambos numeros
#
# Complejidad =  O(8) + O(5n)
# Complejidad = O(n) por teorema 2
#

import sys

def McmNum(n, m):
    
    if n > 0 and m > 0: #O(1)
        if n > m: #O(1)
            maximo = n #O(1)
        else: #O(1)
            maximo = m #O(1)
        while True: #O(5n)
            if maximo % n == 0 and maximo % m == 0: #O(1)
                mcm = maximo #O(1)
                break #O(1)
            maximo += 1 #O(1)

        return mcm #O(1)

    else: #O(1)
        print("Alguno de los numeros es menor que 0") #O(1)
        sys.exit(True) #O(1)


n = int(input("Ingrese el primer número: "))
m = int(input("Ingrese el segundo número: "))

print("El Minimo comun multiplo de los numero es: " + str(McmNum(n, m)))