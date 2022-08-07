from random import randint
sumaNotas=0
mayor=-1
menor=21

for i in range(1,46):
    nota=randint(0,20)
    print("Nota {}: {}".format(i,nota))

    if nota>mayor:
        mayor=nota
    if nota<menor:
        menor=nota
    sumaNotas+=nota

promedio=round(sumaNotas/45,2)
print("Nota mayor: " + str(mayor))
print("Nota menor: " + str(menor))
print("Promedio: " + str(promedio))