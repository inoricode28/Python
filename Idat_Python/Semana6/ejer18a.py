# 46 seguridad 128 vendedor 45 directivo
#Ingreso de datos
codigo = int(input("Ingrese su codigo de 3 digitos: "))
#Proceso
if codigo %2 == 0 and codigo %3 == 0 and codigo %5 ==0:
    tipo = "Administrativo"
elif codigo  %3 == 0 and codigo %5 ==0 and codigo %2 >0:
    tipo = "Directivo"
elif codigo  %2 == 0 and codigo %3 >0 and  codigo %5 >0:
    tipo = "Vendedor"
else:
    tipo = "Seguridad"
#Salida de datos
print("Su tipo de empleado es: " + str(tipo))