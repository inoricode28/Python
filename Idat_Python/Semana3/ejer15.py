#Entrada de datos
cantidad = int(input("Ingrese la cantidad: "))

#Proceso
billetes_100 = cantidad // 100
billetes_50 = cantidad % 100 // 50
billetes_10 = cantidad % 100 % 50 // 10 
moneda_5 = cantidad % 100 % 50 % 10 // 5 
moneda_2 = cantidad % 100 % 50 % 10 % 5 // 2
moneda_1 = cantidad % 100 % 50 % 10 % 5 % 2

#Salida de datos
print ("La cantidad ingresada se desconpondria de la siguiente manera:"  + str(billetes_100),"billetes de 100, " + str(billetes_50),"billetes de 50, " + str(billetes_10),"billetes de 10, " + str(moneda_5),"monedas de 5, " + str(moneda_2),"monedas de 2, " + str(moneda_1),"monedas de 1")