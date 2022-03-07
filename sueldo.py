#Sueldo de un trabajador

nombre=input("Ingrese su nombre: \n -->")
horas=int(input("Ingrese  las horas laboradas: \n -->"))
precio=float(input("Ingrese el precio de las horas laboradas: \n -->"))

Sueldo=horas*precio
mes=Sueldo

print(nombre)
print("Tu Sueldo del dia es: {:.0f}".format(Sueldo))
print("Tu Sueldo del mes es: {:.0f}".format(Sueldo))