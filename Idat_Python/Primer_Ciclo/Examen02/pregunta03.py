#Ingreso de datos

Precio = float(input("Ingrese el Monto: "))
cantidad = int(input("Ingrese la Cantidad a Comprar: "))
#Proceso
ImpCompra = Precio * cantidad

if cantidad >=50:
    des = ImpCompra * 25/100
else:
    des = ImpCompra * 15/100

Imp_pago = ImpCompra - des

#Salida de datos

print ("Importe de Compra es: " + str(ImpCompra))
print ("El des es de: " + str(des))
print ("El importe a Pagar es: " + str(Imp_pago))