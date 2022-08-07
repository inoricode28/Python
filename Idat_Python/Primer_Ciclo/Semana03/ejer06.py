#Entrada de datos
dineroHeredado = int(input("Ingrese la cantidad de dinero que se repartira entre los hijos: "))

#Proceso
Juan = 45/100 * dineroHeredado 
Pablo = 60/100* Juan
Luis = dineroHeredado - Juan - Pablo

#Salida de datos
print ("El dinero se repartira de esta forma: \nJuan recibira: "+ str(Juan))
print ("Pablo recibira: " + str(Pablo))
print ("Luis recibira: "+ str(Luis))