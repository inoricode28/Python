#Entrada de datos
tiempo = int(input("Ingrese la cantidad de tiempo en segundos: "))

#Proceso
horas = tiempo // 3600
minutos = tiempo % 3600 // 60
segundos = tiempo % 3600 % 60 

#Salida de datos
print ("La cantidad ingresada se representaria como: ", "{}:{}:{}" .format(horas,minutos,segundos))