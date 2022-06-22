inferior = int(input("Ingrese extremo inferior del intervalo: "))
superior = int(input("Ingrese extremo superior del intervalo: "))

while inferior<=superior:

    if inferior%2==0:
        print(inferior, end=" ")
    inferior+=1