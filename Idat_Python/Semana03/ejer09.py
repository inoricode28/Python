#Entrada de datos
precioProducto = float(input("Ingresa el precio del producto a comprar: "))
cantidad = int(input("Ingresa la cantidad de unidades adquiridas: "))

#Proceso
importeCompra = precioProducto * cantidad 
descuento = importeCompra * 11/100
importePagar = importeCompra - descuento
chocolates = cantidad * 2

#Salida de datos
print ("El importe de compra es: " + str(importeCompra))
print ("El descuento es de: " + str (descuento))
print ("El importe a pagar es de: " + str (importePagar))
print ("La cantidad de cholates a obsequiar es: " + str (chocolates))