def positivo(num):
    if num > 0:
        return len(str(num))
    else:
        return -1

num = int(input("Ingrese numeros positivo: "))

print(positivo(num))