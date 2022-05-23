#ingresante
categoria=input("Ingrese categoria[A-B-C-D]: ")
nota=float(input("Ingrese nota: "))
#proceso

if categoria=="A":
    mes = 3000
elif categoria=="B":
    mes = 2500
elif categoria=="C":
    mes = 2000
elif categoria=="D":
    mes = 1500

if nota<14:
    des = 0
elif nota>=14 and nota<16:
    des = mes*0.10
elif nota>=16 and nota<18:
    des = mes*0.12
elif nota>=18 and nota<=20:
    des = mes*0.15
NPension=mes-des
print("Mes sin descuento: "+str(mes))
print("Descuento: "+str(des))
print("Nueva pension: "+str(NPension))



