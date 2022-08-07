#ingreso de datos
tiempo=int(input('Ingrese un tiempo en segundo: '))

#Procesos
horas = tiempo//3600 #3600 = 60 minutos * 60 segundos
minutos = tiempo%3600//60
segundos = tiempo%3600%60 # Simplificado seria tiempo%60

#Mostrar resultados
print("{}:{}:{}".format(horas,minutos,segundos))