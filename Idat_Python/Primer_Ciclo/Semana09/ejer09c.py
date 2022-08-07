a,b=0,1

for f in range(30):
    c = b+a
    a = b
    b = c
    print(a,end=" ")