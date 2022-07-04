def calcularMenor(a,b):    
    if a<b:
        return a        
    elif b<a:
        return b       
    else:
         return "Los numeros son iguales"      

numero1 = int(input("1er numero: "))
if numero1>0:
    numero2 = int(input("2do numero: "))
    if numero2>0:
        menor=calcularMenor(numero1,numero2)
        print("el menor es: ", menor)
    else:
        print("El 2do numero debe ser positivo")
else: 
    print("El 1er numero debe ser positivo")
    
