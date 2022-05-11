#1 biblioteca
#2 talleres
#3 investigacio
#4 becas
#5 deporte

# Ingresantes
Donacion = float(input("Ingrese donacion: "))

# Calculo
biblioteca = Donacion * 0.25
talleres = Donacion * 0.20
investigacio = biblioteca * 0.45
becas = (investigacio+talleres) * 0.75
deporte= Donacion-(biblioteca+talleres+investigacio+becas)

# Saliente
print("La biblioteca recibe: ",biblioteca)
print("Los talleres reciben: ",talleres)
print("La investigacio recibe: ",investigacio)
print("La Becas recibe: ",becas)
print("Los deportes recibe: ",deporte)