#f(x) = 28 + (x + ⌊x⁄8⌋) mod 2 + 2 mod x + 2 ⌊1⁄x⌋
import math
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
dias=[31,28,31,30,31,30,31,31,30,31,30,31]
numero_mes=int(input("Ingrese numero del mes: "))

if numero_mes >=1 and numero_mes <=12:    
    print(meses[numero_mes-1],"tiene",dias[numero_mes-1],"dias")
else:
    print("Numero invalido")