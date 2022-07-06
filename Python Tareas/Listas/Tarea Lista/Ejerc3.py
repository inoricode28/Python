Notas_finales = []
acum=0

n = int(input("Cuantas notas decea ingresar: "))

for z in range(n):
    n = int(input("Ingrese nota "+str(z+1)+" :"))
    Notas_finales.append(n)

for a in Notas_finales:
    acum+=a


print(Notas_finales)
print(acum)
