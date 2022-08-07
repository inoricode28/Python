nota=int(input('Ingrese nota: '))
if nota <= 1:
    nota = -1
if nota>=11:
    nota +=2
if nota>21:
    nota = 20

print("La nota es: " + str(nota))