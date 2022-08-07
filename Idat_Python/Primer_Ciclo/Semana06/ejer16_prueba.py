cuota = float (input ('Ingresa el valor de cuota: '))
dia_de_pago = float (input ('Ingresa el valor de dia de pago: '))

recargo=0
if dia_de_pago<=10:
    descuento=cuota*0.02
if dia_de_pago<=10 and descuento<5:
    descuento=5
elif dia_de_pago>10 and dia_de_pago<=20:
    descuento= cuota
elif dia_de_pago>20:
    recargo=cuota*0.03
elif dia_de_pago>20 and recargo<10:
    recargo=10
importe_total_a_pagar=cuota-descuento+recargo
print ('Valor de descuento: ' + repr (descuento))
print ('Valor de importe total a pagar: ' + repr (importe_total_a_pagar))
print ('Valor de recargo: ' + repr (recargo))
