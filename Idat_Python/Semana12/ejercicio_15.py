def facotial(n):
    producto=1
    for i in range(n,0,-1):
        producto*=i
    return producto
numero = int(input("Ingrese un numero: "))
print("EL factorial de {} es: {}".format(numero, facotial(numero)))