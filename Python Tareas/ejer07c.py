a=[]
m=int(input('Ingrese m: '))
n=int(input('Ingrese n: '))

for f in range(m):
    a.append([])
    for c in range(n):
        a[f].append(int(input("Elementos %d, %d : "%(f,c))))
    for f in range(m):
        print('| ',end='')
        for c in range(n):
            print(a[f][c],'| ',end='')
        print()
    print('')
    for f in range(m):

        print('| ',end='')
        for c in range(n):
            if f+c==m-1:
                print(a[f][c], '| ',end='')
            else:
                print('-','| ',end='')
        print()