
"""Cada alumno deberá realizar un programa que tenga 1 función que permita dividir dos
números enteros, a su vez deberá pedir dichos números enteros, el programa debe
tener manejo de excepciones."""
try:
    x=int(input('Ingrese primer numero: '))
    y=int(input('Ingrse segundo numero: '))
    c=x/y
    print("EL resultado es:",c)

except ZeroDivisionError:
    print("No se puede dividir entre 0)")

except ValueError:
    print("Error en los values")
