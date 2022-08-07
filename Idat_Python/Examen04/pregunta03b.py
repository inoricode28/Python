def sumTerm (numero):
    denominador = 4
    numerador = 3
    sum = 4

    for i in range(numero - 1):
        valor = denominador / numerador
        if i % 2 == 0:
            sum -= valor
        else: sum += valor
        numerador += 2
    return sum
        
numero = 1000000
sum = sumTerm (numero)
print (sum)