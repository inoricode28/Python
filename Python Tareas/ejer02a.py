contador = 0
conso=0

cadena = str(input("Ingrese caracter: "))

for letra in cadena:
  if letra.lower() in "aeiou":
    contador += 1
  else:
    conso+=1


print(f"En la cadena hay {contador} vocales",)
print(f"En la cadena hay {conso} vocales",)