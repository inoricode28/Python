def factorial(n):
    producto = 1 
    for i in range(n,0,-1):
        producto*=i
        print(i,end=" ")

    print()   
    return producto

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

def NumeroPerfecto(num):
  suma = 0
  for i in range(1,num):
    if (num % i == 0):
      suma += i
 
  if num == suma:
    return True
  else:
    return False 

def separarParesImpares(lista):
    listaPares=[]
    listaImpares=[]
    for elemento in lista:
        if elemento%2==0:
            listaPares.append(elemento)
        else:
            listaImpares.append(elemento)
    
    return listaPares,listaImpares

def esBisiesto(año):
    if año%400==0:
        return True
    elif año%100==0:
        return False
    elif año%4==0:
        return True
    else:
        return False

def listaBisiestos(inicio, fin):
    lista=[]
    for año in range(inicio,fin+1):
        if esBisiesto(año):
            lista.append(año)
    return lista

