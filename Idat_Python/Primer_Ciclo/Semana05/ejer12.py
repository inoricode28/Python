nota_programacion=float(input('Ingrese nota de F.programacion: '))
nota_DP=float(input('Ingrese nota de D.personal: '))
nota_comunicacion=float(input('Ingrese nota de comunicacion: '))

if nota_programacion>=0 and nota_programacion<=20 and nota_DP>=0 and nota_DP<=20 and nota_comunicacion>=0 and nota_comunicacion<=20:
    if nota_programacion>17:
        propina_progra = int(nota_programacion)*3
    else:
        propina_progra = int(nota_programacion)*1
    if nota_DP>15:
        propina_DP = int(nota_DP)*2
    else:
        propina_DP = int(nota_DP)*0.5
    if nota_comunicacion>16:
        propina_comu = int(nota_comunicacion)*1.5
    else:
        propina_comu = int(nota_comunicacion)*0.30
    propina_total=propina_progra+propina_DP+propina_comu
    if nota_programacion>18:
        obsequio="Ganaste un reloj"
    else:
         obsequio="Ganaste un lapicero"
    print("El total de propinas es: "+str(propina_total))
    print("El Obsequieo es: " + obsequio)
else:
    print("Nota incorrecta") 


