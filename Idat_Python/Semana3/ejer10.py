#Ingreso de datos
precio=float(input('Precio de la camisa: '))
cantidad=int(input('Cantidad de camisas: '))

#Proceso

importeCompra= precio * cantidad
primerDesccuento = importeCompra*7/100
segundoDescuento = (importeCompra-primerDesccuento)*7/100
descuentoTotal= primerDesccuento+segundoDescuento
importePagar = importeCompra- descuentoTotal

#Mostrar resultado
print("Importe de compra: " + str(importeCompra))
print("Importe 1er descuento: " + str(primerDesccuento))
print("Importe 2do descuento: " + str(segundoDescuento))
print("Importe descuento total: " + str(descuentoTotal))
print("Importe a pagar: " + str(importePagar))