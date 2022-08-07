import random
print("Numero\t","Cantidad de divisores")
divisores=0
while(divisores!=4):
    numero=random.randint(1,1000)
    t=0
    divisores=0
    while(t<=numero):
        t+=1
        if(numero%t==0): divisores+=1
    print(numero,"\t",divisores)