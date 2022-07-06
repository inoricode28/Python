"""
Ingresar por teclado y almacenar en una lista las alturas de
5 personas(metros). Obtener el promedio de las mismas. Contar 
cuantas personas son mas altas que el promedio y cuantas mas bajas
"""
alturas = []
suma = 0

for x in range(5):
    a = float(input("Ingrese altura "+ str(x+1)+" :"))
    alturas.append(a)
    suma+=a

print("Las alturas ingresadas son")
print(alturas)
prom = suma/5
print(f"El promedio de las alturas son: {prom}")

alto=0
bajo=0

for z in range(5):
    if alturas[z]>prom:
        alto+=1
    else:
        bajo+=1

print(f"La cantidad de personas mas altas al promedio es: {alto}")
print(f"La cantidad de personas mas bajas al promedio es: {bajo}")
