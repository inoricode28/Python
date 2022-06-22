n=30
tpar,suma,r=5,0,0
for i in range(1,n+1):
    if(i%2!=0): 
        r=int(2**((i+1)/2))
        print(r,end=",")
    else: 
        tpar+=2
        print(tpar,end=",")
        r=tpar
    suma+=r
print("\nLa suma es: "+str(suma))