turno=str(input('Ingrese el turno: '))
cantidad=int(input("Cantidad: "))

if turno=="mañana":
    monto = 37.5*cantidad
else:
    monto=45*cantidad

if cantidad>=15:
    descuento = monto*8/100
else:
    descuento = monto*5/100

importeFinal = monto - descuento

if importeFinal>200:
    caramelos = cantidad*2
else:
    caramelos = 0

#Salida
print("El importe de compra es de: " + str(monto))
print("El importe de descuento es de : " + str(descuento))
print("El importe a pagar: " + str(importeFinal))
print("El importe de caramelos a obsequiar es de: " + str(caramelos))