#Ingreso de datos
equipoA=int(input("Goles de l quipo \"A\": "))
equipoB=int(input("Goles del quipo \"B\": "))

#Proceso
if equipoA>equipoB:
    resultado = "Gano el quipo \"A\""
if equipoB>equipoA:
    resultado="Gano el quipo \"B\""
if equipoA==equipoB:
    resultado="Empate"

#Mostrar resultados
print(resultado)
