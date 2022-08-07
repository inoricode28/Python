from random import randint

cantmultiplo3=0
for i in range(100,900):
    if i%3==0:  
        print(i,end=" ")
        cantmultiplo3+=1

print("\nLa cantidad de multiplos de 3 son: "+str(cantmultiplo3))
        
