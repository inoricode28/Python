suma = 0
for n in range(0,60):
    suma += (3*n+2)/(4*n+5)
    print(f"{3*n + 2}/{4*n + 5}",end=",")
    if (n+1)%12==0:
        print()

print(f"La suma es {suma:.3f}")