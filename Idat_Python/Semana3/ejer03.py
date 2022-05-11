#Entrada de datos
horasTrabajas = int(input("Ingresar la cantidad de horas trabajadas: "))
tarifaHora = float(input("Ingrese la tarifa por hora: "))

#Proceso
sueldoBasico = horasTrabajas * tarifaHora
bonificacion = 20/100 * sueldoBasico
sueldoBruto = sueldoBasico + bonificacion
descuento = 10/100 * sueldoBruto
sueldoNeto = sueldoBruto - descuento

#Salida de datos
print ("El sueldo basico del trabajador es: " + str(sueldoBasico))
print ("La bonificación del trabajador es: " + str(bonificacion))
print ("El sueldo bruto del trabajador es: " + str(sueldoBruto))
print ("El descuento del trabajador es: " + str(descuento))
print ("El sueldo neto es: " + str(sueldoNeto))