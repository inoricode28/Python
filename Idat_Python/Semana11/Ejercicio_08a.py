#f(x) = 28 + (x + ⌊x⁄8⌋) mod 2 + 2 mod x + 2 ⌊1⁄x⌋
import math
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
numero_mes=int(input("Ingrese numero del mes: "))

if numero_mes >=1 and numero_mes <=12:    
    
    Numero_dias=28+(numero_mes+math.floor(numero_mes/8))%2+2%numero_mes+2*math.floor(1/numero_mes)
    print(meses[numero_mes-1],"tiene",Numero_dias,"dias")
else:
    print("Numero invalido")