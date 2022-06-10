from random import randint

cantAprobador=0
cantDesaprobados=0
sumaNotas=0
for i in range(40):
    nota = randint(0,20)
    sumaNotas+=nota
    print(nota, end=" ")
    if nota>=13:
        cantAprobador+=1
    else:
        cantDesaprobados+=1

promedio = sumaNotas/40

print("\nNota promedio: "+str(promedio))
print("Cantidad aprobados: "+str(cantAprobador))
print("Cantidad Desaprobados: "+str(cantDesaprobados))



