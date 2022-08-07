d=1
n=2
suma=0
for i in range(1,51): 
    print(d, "/", n )
    suma+=d/n
    d+=4
    n*=3

print("\nLa suma es: " + str (suma))