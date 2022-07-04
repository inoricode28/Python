# no contamos ni el 1, por que el 1 siempre es divisor, el rango toma valores entre dos y numero -1
def NumeroPerfecto(num):
  suma = 1
  for i in range(2,num):
    if (num % i == 0):
      suma += i
 
  if num == suma:
    return True
  else:
    return False
 
num = int(input("introduzca un numero:"))
 
if NumeroPerfecto(num):
  print("%s es un numero perfecto" % num)
else:
  print("%s NO es un numero perfecto" % num)