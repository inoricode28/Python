#Encontrar los numeros repetidos de una lista

numeros = [2,3,5,1,4,3,6,7,9,5,8]

repetidos=[]
archivo = []
for n in numeros:
    if n not in archivo:
        archivo.append(n)
    else:
        repetidos.append(n)

print(repetidos)
