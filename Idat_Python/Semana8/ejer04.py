i=2
y=5
numerador=0
denominador=0
contador=0
while contador<50:
    print(i,end="/")
    print(y,end=" ")
    numerador+=i #Acumulador
    i+=3
    denominador+=i #Acumulador
    y+=4
    contador+=1 #Contador
print("\nN° terminos: "+str(contador))
