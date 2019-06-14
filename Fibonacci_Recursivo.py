# 6)Hacer una funcion que calcule el n-ésimo 
# número de la serie de fibonacci,
#
# Pre: n >= 0 El numero ingresado debe ser positivo o 0
# Post: Entrega el valor del n número de la serie de fibonacci
#

def fibonacci(num):
    if num == 0 or num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

print("Sucesión Fibonacci Recursiva")
num=int(input("Ingresa el numero de la serie: "))
resutado=fibonacci(num)
print("El numero de la sucesión numero " + str(num) + " de fibonacci es el : " + str(resutado))

