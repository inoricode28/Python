#Ingreso de datos
importeVendido=float(input('Importe Vendido: '))
numHijos=int(input('Numero de hijos: '))
sueldoBasico = 600
if importeVendido>15000:
    comision= importeVendido*7/100
else:
    comision= importeVendido*5/100

if numHijos<5:
    bonificacion = numHijos*25
else:
    bonificacion = numHijos*22

sueldoBruto = sueldoBasico+comision+bonificacion

if sueldoBruto>3500:
    descuento = sueldoBruto*15/100
else:
    descuento = sueldoBruto*11/100

sueldoNeto = sueldoBruto - descuento

#Mostrar resultados
print("Su comision es de: "+str(comision))
print("Su bonificacion es de: "+str(bonificacion))
print("Su sueldo bruto es de: "+str(sueldoBruto))
print("Su descuento es de: "+str(descuento))
print("Su sueldo neto es de: "+str(sueldoNeto))