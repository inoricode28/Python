cantidad=int(input("Cantidad de pasaje: "))
turno=(input("Ingrese turno ('mañana' o 'noche'): "))
######################################################
if turno != "mañana" or turno!= "noche":
    pasaje = -1#try
if turno =="mañana":
    pasaje=37.5
else:
    pasaje = 45
######################################################
importeCompra = cantidad*pasaje
######################################################
if cantidad >=15:
    descuento = importeCompra* 0.08
else:
    descuento = importeCompra * 0.05
######################################################
importePagar = importeCompra - descuento
######################################################
if importePagar>200:
    caramelos = cantidad * 2
else:
    caramelos = 0

if pasaje == -1:#catch
    print("Ingrese un turno correcto")
else:
    print("El importe de compra es: S/."+str(importeCompra))
    print("El importe de descuento es: S/."+str(descuento))
    print("El importe a pagar es: S/."+str(importePagar))
    print("El total de caramelos es: S/."+str(caramelos))