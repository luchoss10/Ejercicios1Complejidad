# 2) Hacer una función que reciba un valor N 
# y retorne la sumatoria de los eneros hasta N 
#
# Pre: N>=1 El número N debe ser mayor que 1 para empezar la sumatoria
# Post: Se debe entregar la suma de todos los numeros hasta el numero N
#

def sumatoria(n):
    if n >=1:
        j = 0
        for i in range(0, n):
           j = i+j
        return j
    else:
        return "El numero es negativo"
    

num = int(input("Ingrese un numero para sumatoria: "))

print(str(sumatoria(num)))



