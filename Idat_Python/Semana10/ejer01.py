from random import randint
cont= 1
while True:    
    year= randint(25,80)
    state= randint(1,4)

    if state==1:
        state= ("Soltero")
    elif state==2:
        state=("Casado")
    elif state==3:
        state=("Viudo")
    else:
        state=("Divorciado")
    print("Persona N°",cont, "tiene edad: ",year,"y state civil:",state)
    if year ==80:
        break
    cont+=1