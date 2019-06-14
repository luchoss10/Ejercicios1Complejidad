# 7)Hacer una función que retorne el mcm(mínimo común múltiplo)
# de 2 números naturales mayores que 0
#
# Pre: n y m > 0 los numeros introducidos deben ser mayores que 0
# Post: Entrega el mcm de ambos numeros
#

import sys

def McmNum(n, m):
    
    if n > 0 and m > 0:
        if n > m:
            maximo = n
        else:
            maximo = m
        while True:
            if maximo % n == 0 and maximo % m == 0:
                mcm = maximo
                break
            maximo += 1

        return mcm

    else:
        print("Alguno de los numeros es menor que 0")
        sys.exit(True)


n = int(input("Ingrese el primer número: "))
m = int(input("Ingrese el segundo número: "))

print("El Minimo comun multiplo de los numero es: " + str(McmNum(n, m)))