lista=[]
par=0
impar=0
y=0
n = int(input("Cuantos numeros desea ingresar: "))

for z in range(1,n+1):
    #num=int(input("Ingrese numero: "))
    lista.append(y+1)
    y+=1
    if y%2==0:
        par+=1
    else:
        impar+=1

print(lista)
print("Par:",par,"Impar:",impar)

""" OTRA FORMA
lista=[]
par=0
impar=0

n = int(input("Cuantos numeros desea ingresar: "))

for z in range(n):
    num=int(input("Ingrese numero: "))
    lista.append(num)

for j in lista:
    if j % 2 == 0:
        par+=1
    else:
        impar+=1

print(par, impar)
"""