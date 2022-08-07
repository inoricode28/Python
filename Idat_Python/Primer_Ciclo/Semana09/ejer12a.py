i=1
y=1
numerador=0
denominador=0
contador=0
for g in range(15):
    print(i,end="/")
    print(y,end=" ")
    numerador+=i #Acumulador
    i+=5
    denominador+=i #Acumulador
    y+=4
    contador+=1 #Contador
print("\nN° terminos: "+str(contador))

