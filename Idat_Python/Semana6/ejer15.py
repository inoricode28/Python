chocoNum=int(input('Ingrese tipo de chocolate[1-2-3-4]: '))
cantidad=int(input('Ingrese cantidad: '))
if chocoNum==1:
    Punit = 8.5
elif chocoNum==2:
    Punit = 10
elif chocoNum==3:
    Punit = 7
elif chocoNum==4:
    Punit = 12.5

importe_Compra=cantidad*Punit

if cantidad<5:
    des = importe_Compra*4/100
elif cantidad>=5 and cantidad<10:
   des = importe_Compra*6.5/100
elif cantidad>=10 and cantidad<15:
    des = importe_Compra*9/100
elif cantidad>=15:
    des = importe_Compra*11/100

importe_Pagar=importe_Compra-des

if importe_Pagar>250:
    obsequio=cantidad*3
else:
    obsequio=cantidad*2

print("El importe de compra es: "+str(importe_Compra))
print("El Descuento es: "+str(des))
print("El importe de pagar es: "+str(importe_Pagar))
print("El obsequio es: "+str(obsequio))