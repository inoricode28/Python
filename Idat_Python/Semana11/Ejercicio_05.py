listaProductos=[]
listaPrecios=[]

for i in range(5):
    producto=input("Ingrese un producto: ")
    listaProductos.append(producto)
    precio=float(input("Ingrese el precio: "))
    listaPrecios.append(precio)

print("Producto\tPrecio")
for i in range(len(listaProductos)):
    print("{}\t\t{}".format(listaProductos[i],listaPrecios[i]))
