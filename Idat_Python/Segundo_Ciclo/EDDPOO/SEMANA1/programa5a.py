from random import randint
dado1 = randint(1,6)
dado2 = randint(1,6)

print(dado1)
print(dado2)

if dado1 + dado2 == 9:
    print("Has ganado")
else:
    print("Perdiste")