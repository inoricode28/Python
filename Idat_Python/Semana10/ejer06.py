i=5
suma=0
contador=0
while contador<50:
    print(i,end=" ")
    suma+=i #Acumulador
    i+=6
    contador+=1 #Contador
print("\nsuma: "+str(suma))
print("N° terminos: "+str(contador))