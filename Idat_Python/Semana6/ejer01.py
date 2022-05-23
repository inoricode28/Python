#ingresante de datos
golesA=int(input('Goles A: '))
golesB=int(input('Goles B: '))

#Proceso
if golesA>golesB:
    resultado ="Gano A"
elif golesB>golesA:
    resultado="Gano B"
else:
    resultado="Empate"

#Mostrar resultados
print(resultado)