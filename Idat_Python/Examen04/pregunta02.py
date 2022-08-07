def numEntero(numero):
    if len(str(numero))>=3 and numero>0:
        v1=len(str(numero))
        v2=10**(int(v1)-1)
        return(numero%v2)//10
    else: 
        return "Numero no valido" 

numero= 486237
final=numEntero(numero)
print(final)