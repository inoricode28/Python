n=int(input('Ingrese numero: '))
x=1
contador=0
while x<=n:
    if n%x==0:
        print(x,end=" ")
        contador+=1
    x+=1
print("\nContador: " + str(contador))
