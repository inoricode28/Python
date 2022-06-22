monto=float(input('Ingrese monto a pagar: '))
if not(monto>0):
    mensaje= "Monto no es valido"
    print(mensaje)
else:
    if monto<=5000:
        mensaje="2 cuotas "
        cuota=monto/2
        interes = (cuota*0.05)*2
    elif monto>5000 and monto<=10000:
         mensaje="4 cuotas "
         cuota=monto/4
         interes = (cuota*0.05)*4
    elif monto>10000 and monto<=15000:
         mensaje="6 cuotas "
         cuota=monto/6
         interes = (cuota*0.03)*6
    elif monto>15000:
         mensaje="10 cuotas "
         cuota=monto/10
         interes = (cuota*0.03)*10   
print("Son "+str(mensaje))
print("Cuota mensual "+str(cuota))
print("Monto total de intereses "+str(interes))
#print(mensaje + str(cuota)+" mensual")
#print(mensaje+"interes son "+str(interes))    