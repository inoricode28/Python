from random import randint

cantidad=0
while True:
    d1=randint(1,6)
    d2=randint(1,6)
    print(d1,d2, sep="-",end=" ")
    cantidad+=1
    if d1==6 and d2==6:
        break
print("\nCantidad de lanzamiento: "+str(cantidad))

