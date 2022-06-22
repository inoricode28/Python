#ingreso de datos
sexo=(input('Sexo Maculino(M), Femenino(F): '))
edad=int(input('Edad: '))
#Proceso
if sexo == "F":
    if edad<23:
        categoria = "FA"
    else:
        categoria = "FB"
else:
    if edad <23:
        categoria = "FA"
    else:
        categoria = "FB"

#Mostrar resultados
print("Categoria: "+categoria)