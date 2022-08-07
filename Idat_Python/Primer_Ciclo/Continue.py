i=0 #Valor inicial
while i<=5:#Mientras se a verdad
    i+=1#Contador
    if i==3:#Salta el numero 3
        continue
    print("Dentro del ciclo.",i)
print("Fuera del ciclo.")