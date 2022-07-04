def esBisiesto(año):
    if año%400==0:
        return True
    elif año%100==0:
        return False
    elif año%4==0:
        return True
    else:
        return False

#Estos son algunos ejemplos de posibles respuestas:
#2012 es bisiesto,
#2010 no es bisiesto
#2000 es bisiesto,
#1900 noe s bisisestro.

print(2012,esBisiesto(2012))
print(2010,esBisiesto(2010))
print(2000,esBisiesto(2000))
print(1900,esBisiesto(1900))
