precio_ciento=float(input('Ingrese precio por ciento: '))
cantidad_ciento=int(input('Ingrese la cantidad de  ciento de papel: '))

if cantidad_ciento<=0 or precio_ciento<=0:
     print("Precio u Hojas invalidas")
else:
    if cantidad_ciento<=5:
        descuento = precio_ciento*cantidad_ciento*0.10
        precio_bruto = precio_ciento*cantidad_ciento
        precio_total = precio_bruto-descuento
        print("El precio bruto  es: S/ "+str(precio_bruto))
        print("El descuento es: S/ "+str(descuento))
        print("El precio total es: S/ "+str(precio_total))
    else:
        descuento = precio_ciento*cantidad_ciento*0.15
        precio_bruto = precio_ciento*cantidad_ciento
        precio_total = precio_bruto-descuento
        print("El precio bruto  es: S/ "+str(precio_bruto))
        print("El descuento es: S/ "+str(descuento))
        print("El precio total es: S/ "+str(precio_total))
        
        

