import numpy as np
print("Brainly")
n=int(input("Escriba un entero: "))
matriz=np.random.randint(1,20,(n,n))
print("Matriz")
print(matriz)
print("\ndiagonal")
for x in range (n):
    print(matriz[x,-x-1])