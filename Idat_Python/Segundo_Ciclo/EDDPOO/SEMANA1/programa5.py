import random 
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
suma = dado1 + dado2

print("Dado 1: ",dado1)
print("Dado 2: ",dado2)

if suma == 9:
    print("Has ganado")
else:
    print("Perdiste")