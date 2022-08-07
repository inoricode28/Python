import random
numero,cantidad=1000,0
while(numero<=9999):
    n=str(numero)
    impar,par,t=0,0,4
    while(t>0):
        t-=1
        if(int(n[t])%2==0): par+=int(n[t])
        else: impar+=int(n[t])
    if(par==impar):
        cantidad+=1
        print("numero=",n,"SumaPar=",par,"SumaImpar",impar)
    numero+=1
print("Cantidad de numeros entontrados",cantidad)