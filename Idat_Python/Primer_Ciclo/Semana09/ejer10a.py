while True:
    n=int(input("Ingrese numero: "))
    a,b,suma=3,4,0
    for i in range(0,n):
        print(a,b,sep="/")
        suma+=a/b
        a+=2
        b+=3
    print("suma=",suma)