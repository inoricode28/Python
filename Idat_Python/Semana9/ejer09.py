a=0
b=1
for n in range(30):
    if n<1:
        resul=n
        print(resul,end=",")
    else:        
        c = b+a
        a = b
        b = c
        print(a,end=",")
