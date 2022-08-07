from random import randint
n=int(input('Ingrese numero de edades: '))
inicio=1

while inicio<=n:
    edad= randint(25,80)
    estado= randint(1,4)
    if estado==1:
        print(edad,"Soltero")
    elif estado==2:
        print(edad,"Casado")
    elif estado==3:
        print(edad,"Viudo")
    elif estado==4:
        print(edad,"Divorciado")
    inicio+=1
    
