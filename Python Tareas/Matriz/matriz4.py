"""
Crear un matriz(lista de lista) que almacene el importe de la compra de 10
productos de 3 clientes. Almacene en una vector(lista)el importe total 
por cliente y muestre los valores
"""

imp = []
total = []
for i in range(3):
    imp.append([])
    for j in range(3):
        imp[i].append(int(input("Ingrese el importe del producto "+str(i+1)+" , cliente "+
        str(j+1)+ " :")))

for i in range(3):
    suma=0
    for j in range(3):
        suma=suma+imp[j][i]
    total.append(suma)

print("El importe de todos los productos por cliente son: ")
print(total)
print(f"Cliente 1 = ${total[0]}, Cliente 2 = ${total[1]}, Cliente 3 = ${total[2]}")