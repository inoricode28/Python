razonPar,razonImpar,suma,r=1,7,0,0

for i in range(2,27):
    if i%2==0:
        r=2**razonPar
        print(r,end=",")
        razonPar+=1
        
    else:        
        print(razonImpar,end=",")
        razonImpar+=2
        r=razonImpar
    suma+=r

print("\nLa suma es: ",suma)