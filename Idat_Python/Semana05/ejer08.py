#Ingreso de datos
turno=int(input('Ingrese el turno Mañana(1), Noche(2): '))
cantidad=int(input('Ingrese la cantidad: '))
#Procesar
if turno ==1:
    precio=37.5
else:
    precio = 45

importeCompra = precio*cantidad

if cantidad>=15:
    descuento = importeCompra*8/100
else:
    descuento = importeCompra*5/100

importePagar= importeCompra-descuento

if importePagar>200:
    caramelo = cantidad*2
else:
    caramelo = 0

#Mostrar resultados
print("Importe de compra: " + str(importeCompra))
print("Descuento: " + str(descuento))
print("Importe a pagar: " + str(importePagar))
print("Caramelos de obsequio: " + str(caramelo))
 
