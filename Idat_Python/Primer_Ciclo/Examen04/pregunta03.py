from decimal import Decimal

def custom_function(x):
    numerador = 4*(-1)**(x+1)
    denominador = 2*x -1
    result = Decimal(numerador)/Decimal(denominador)
    return result

def sumatoria(y):
    result = 0
    for i in range(1, y+1):
        result = result + custom_function(i)
    return result

n = int(input('Ingrese: '))
print(sumatoria(n))