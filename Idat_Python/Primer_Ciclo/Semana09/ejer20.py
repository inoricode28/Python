from random import randint

unhijo=0
doshijos=0
treshijos=0
cuatrohijos=0

for i in range(75):
    hijos = randint(1,5)
    
    if hijos==1:        
        unhijo+=1
    elif hijos==2:
        doshijos+=1
    elif hijos==3:
        treshijos+=1
    elif hijos==4:
        cuatrohijos+=1


print("Un solo hijo: "+str(unhijo))
print("Un solo hijo: "+str(doshijos))
print("Un solo hijo: "+str(treshijos))
print("Un solo hijo: "+str(cuatrohijos))
    

