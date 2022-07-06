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

from operator import le
import random

estado = ["Municipio_1", "Municipio_2", "Municipio_3", "Municipio_4", "Municipio_5" ]
cantidatos = ["Candidato_1", "Candidato_2", "Candidato_3", "Candidato_4" ]
votos = []
votos_total = []

for z in range(len(cantidatos)):
    votos.append([])
    for x in range(len(estado)):
        votos[z].append(random.randint(1, 40))

print(votos)


for z in range(len(cantidatos)):
    suma = 0
    for i in range(len(estado)):
        suma = suma + votos[z][i]
    votos_total.append(suma)

sum = votos_total[0] + votos_total[1] + votos_total[2] + votos_total[3]
print(sum)
for i in range(0, 4):
    m1 =votos_total[i] * 100 / sum  
    print("Municipio ",str(i+1),": ",votos_total[i],"votos ",round(m1, 2),"%" )

# M1 = votos_total[0] * 100 / sum
# print(round(M1, 2),"%")
# print("Municipio 1: ",votos_total[0],"Municipio 2: ",votos_total[1],"Municipio 3: ",votos_total[2],"Municipio 4: ",votos_total[3])
