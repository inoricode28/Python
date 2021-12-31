ApeNom=input("Ingrese Nombre y Apellido: \n -->")
NumeHora=int(input("Ingrese Numero de horas laboradas: \n -->"))
HoraTraba=float(input("Ingrese Precio por hora laboradas: \n -->"))
##Realizar calculo
Sueldo=float(NumeHora*HoraTraba)
Dscto=float(Sueldo*(12/100))
Neto=float(Sueldo-Dscto)
print (ApeNom)
##print ("El sueldo basico es %d"%(Sueldo)) este comando saca enteros
print ("El sueldo basico es {:.2f}".format(Sueldo))
print ("El descuento de ley es {:.2f}".format(Dscto))
print ("El neto a pagar es {:.2f}".format(Neto))
