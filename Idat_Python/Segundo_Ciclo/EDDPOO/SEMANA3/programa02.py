'''
Elabore un algoritmo que compruebe si una cadena leída por teclado comienza por una subcadena introducida por teclado.
'''
cad = input("Ingrese la cadena: ").upper()
subcad = input("Ingrese una subcadena: ").upper()
if cad.startswith(subcad):
    print("La cadena comienza por la subcadena...!!!")
else:
    print("La cadena NO comienza por la subcadena...!!!")