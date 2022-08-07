inicio=5
suma=0
for i in range(1,21):
    suma+=inicio
    print(inicio,end=" ")
    inicio+=6
    if i%5==0:
        print()
    
print("\nLa suma es: ",str(suma))     
    