importe=float(input("Ingrese importe: \n -->"))
porcentaje=float(input("Ingrese IGV: \n -->"))

porcentaje=porcentaje/100
IGV=importe*porcentaje
total=importe+IGV

print("Su IGV es: {:.0f}".format(IGV))
print("Su importe a pagar es: {:.0f}".format(total))