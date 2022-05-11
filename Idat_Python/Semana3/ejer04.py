#Entrada de datos
monica = int(input("Ingrese la cantidad de Monica: "))
rachel = int(input("Ingrese la cantidad de Rachel: "))
phoebe = int(input("Ingrese la cantidad de Phoebe: "))

#Proceso
capital = monica + rachel+ phoebe
monicaPorcentaje =  monica * 100 / capital
rachelPorcentaje = rachel * 100 / capital
phoebePorcentaje = phoebe * 100 / capital

#Salida de datos
print ("El capital en total acumulado es: " + str(capital))
print ("El porcentaje aportado por Monica es de: " + str(monicaPorcentaje ),"%")
print ("El porcentaje aportado por Rachel es de: " + str(rachelPorcentaje),"%")
print ("El porcentaje aportado por Phoebe es de: " + str(phoebePorcentaje),"%")