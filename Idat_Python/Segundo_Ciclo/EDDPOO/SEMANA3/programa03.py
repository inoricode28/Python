'''
Elabore un programa que pida una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.
'''
nombre=input('Ingrese su nombre: ')

while True:
    carater = input('Ingrese un caracter: ')
    if len(carater)==1:
        break

print("El caracter aparecer",nombre.count(carater),"veces")
