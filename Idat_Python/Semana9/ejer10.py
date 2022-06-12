#2n+1 / 2n+1+n
suma = 0
for n in range(1,10):
    suma += (2*n+1)/(2*n+1+n)
    print(f"{2*n + 1}/{2*n + 1 + n}")

print(f"La suma es {suma:.3f}")