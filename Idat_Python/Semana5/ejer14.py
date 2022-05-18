compra=float(input('Ingrese compra: '))
numero_Oculto=int(input('Ingrese numero oculto: '))

if numero_Oculto<=99 or compra<=0:
    print("Numero o compra es incorrecta")
else:
    if numero_Oculto%2==0:
        descuento=compra*0.15
        total_Pagar= compra-descuento
    else:
        descuento=compra*0.05
        total_Pagar= compra-(descuento)
    print("Importe es: " + str(compra))
    print("Descuento es: " + str(descuento))
    print("Importe es: " + str(total_Pagar))
