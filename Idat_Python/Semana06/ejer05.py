#Ingreso de datos
codigo=int(input("Codigo de producto(101-102-103): "))
unidades=int(input('Unidades: '))

#Procesos
if codigo ==101: 
    precioUnitario = 17.5
elif codigo ==102:
    precioUnitario=25
elif codigo ==103:
    precioUnitario=15.5

importeCompra= precioUnitario*unidades

if unidades>=1 and unidades<=10:
    descuento = importeCompra*5/100
elif unidades>=11 and unidades<=20:
    descuento= importeCompra*7.5/100
elif unidades>20:
    descuento= importeCompra*10/100

importePagar= importeCompra-descuento

#Mostrar Resultados
print("Importe de compra: " + str(importeCompra))
print("Descuento: " + str(descuento))
print("Importe a pagas: " + str(importePagar))