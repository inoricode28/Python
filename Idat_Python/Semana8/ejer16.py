from random import randint
t,maximo,minimo,suma_notas=45,0,20,0
while(t>0):
    t-=1
    nota=randint(0,20)
    if(nota<minimo): minimo=nota
    if(nota>maximo): maximo=nota
    print("alumno",45-t,"nota=",nota)
    suma_notas+=nota
promedio=suma_notas/45
print("promedio=",promedio)
print("nota maxima",maximo)
print("nota minima",minimo)