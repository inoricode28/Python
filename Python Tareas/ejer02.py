def contar_vocales(cadena):
  vocal = 0  
  for letra in cadena:
    if letra.lower() in "aeiou":
      vocal += 1    
  return vocal

def contar_consonante(cadena):
  consonante = 0
  for letra in cadena:
    if letra.lower() != "aeiou":
      consonante += 1
  return consonante


cadena = str(input("Ingrese caracter: "))

catVocales = contar_vocales(cadena)
print(f"En la cadena hay {catVocales} vocales")
catConsonantes = contar_vocales(cadena)
print(f"En la cadena hay {catConsonantes} Consonantes")