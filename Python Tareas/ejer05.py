lista=[]
par=0
impar=0
y=0
n = int(input("Cuantos numeros desea ingresar: "))

for z in range(1,n+1):
    lista.append(y+1)
    y+=1
    if y%2==0:
        par+=1
    else:
        impar+=1

print(lista)
print("Par:",par,"Impar:",impar)
