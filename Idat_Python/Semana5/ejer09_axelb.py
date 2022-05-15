#Ingreso de datos

sexo = input("Ingrese el genero Femenino (F), Masculino (M)): ")
edad = int(input("Ingrese su edad: "))

#Proceso

if sexo == "F": 
    if edad <23:
       categoria = "FA"
    else:
       categoria = "FB"

else:
    if edad <25:
       categoria = "MA"
    else:
       categoria = "MB"   

#Salida de datos

print ("Su categoria es: " + str(categoria))