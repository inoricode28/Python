vocal = 0
cosonante=0

cadena = str(input("Ingrese caracter: "))

for letra in cadena:
	if letra.lower() in "aeiou":
		vocal += 1
	else:
		cosonante+=1


print(f"En la cadena hay {vocal} vocales")
print(f"En la cadena hay {cosonante} vocales")
