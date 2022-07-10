"""
Se tienen los resultados de las últimas elecciones para alcalde en el estado X, 
el cual está conformado por 5 municipios. 
En dichas elecciones hubo 4 candidatos. Haga un programa que:
a)Lea e imprima una tabla indicando los votos obtenidos en cada municipio por 
    los 4 candidatos.
b)Calcule el total de votos recibidos por cada candidato y el porcentaje 
    del total de votos emitidos.
c)Calcule el candidato más votado.
"""

import random


Minicipio = 5
cantidatos = 4
votos = []
votos_total = []


for z in range(cantidatos):
    votos.append([])
    for x in range(Minicipio):
        votos[z].append(random.randint(10, 90))

print("-------------C1"," C2"," C3"," C4"," C5--------------")

for i in range(cantidatos):
    print("Minicipio",str(i+1),votos[i])

print()
    
filas = len(votos)
columnas = len(votos[0])

for j in range(columnas):
    suma = sum([filas[j] for filas in votos])
    votos_total.append(suma)


print("--------------C1"," C2"," C3"," C4"," C5--------------")
print("V. total x C", votos_total[0],votos_total[1],votos_total[2],votos_total[3],votos_total[4])

sum = votos_total[0] + votos_total[1] + votos_total[2] + votos_total[3]
porcentaje = []
for i in range(0, 5):
    m1 =votos_total[i] * 100 / sum  
    print("Candidato",str(i+1),": ",votos_total[i],"votos ",round(m1, 2),"%")
    porcentaje.append(round(m1, 2))

# print(porcentaje)

candidatos = [["Candidato 1", votos_total[0], porcentaje[0]],["Candidato 2", votos_total[1], porcentaje[1]], ["Candidato 3", votos_total[2], porcentaje[2]], ["Candidato 4", votos_total[3], porcentaje[3]], ["Candidato 5", votos_total[4], porcentaje[4]] ]

print("--------------------------------------Votos ""Pocentaje-------------------------")
print("Candidato mas votado: ",max(candidatos),"%")
