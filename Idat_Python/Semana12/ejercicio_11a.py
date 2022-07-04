# no contamos ni el 1, por que el 1 siempre es divisor, el rango toma valores entre dos y numero -1
def NumeroPerfecto(num):
  suma = 0
  for i in range(1,num):
    if (num % i == 0):
      suma += i
 
  if num == suma:
    return True
  else:
    return False 