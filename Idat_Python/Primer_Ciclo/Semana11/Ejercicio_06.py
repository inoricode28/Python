listaNotas=[]
for i in range(1,6):
    nota=int(input("Ingrese la nota N° "+str(i)+": "))
    listaNotas.append(nota)
indPosMayor=0
indPosMenor=0
mayor=listaNotas[0]
menor=listaNotas[0]
suma=listaNotas[0]

for i in range(1,len(listaNotas)):
    if listaNotas[i]>mayor:
        mayor=listaNotas[i]
        indPosMayor=i
    if listaNotas[i]<menor:
        menor=listaNotas[i]
        indPosMenor=i
    suma+=listaNotas[i]
    
promedio= suma/len(listaNotas)
print("Notas: ",listaNotas)
print("Notas mayor: {} se encuentra en la posicion: {}".format(mayor,indPosMayor))
print("Notas mayor: {} se encuentra en la posicion: {}".format(menor,indPosMenor))
print("Notas menor: ",menor)
print("Promedio: ",promedio)