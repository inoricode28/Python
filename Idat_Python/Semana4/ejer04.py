#ingresante
promedio=float(input("Promerio: "))

#Proceso
if promedio>=17:
    categoria = "A"
if promedio>=14 and promedio<17:
    categoria = "B"
if promedio>=12 and promedio<14:
    categoria = "C"
if promedio<12:
    categoria = "D"

#Mostrar resultado
print("Categoria: " + categoria)