#Entrada de datos
#from turtle import st
importeVendido = int(input("Ingrese el importe total vendido: "))

#Proceso
sueldoBasico = 750
comision = importeVendido * 5/100
sueldoBruto = sueldoBasico + comision
descuento = sueldoBruto * 15/100
sueldoNeto = sueldoBruto - descuento

#Salida de datos
print ("Sueldo basico: " + str(sueldoBasico))
print ("Comisión: " + str(comision))
print ("Sueldo Bruto: " + str(sueldoBruto))
print ("Descuendo: " + str(descuento))
print ("Sueldo Neto: " + str(sueldoNeto))