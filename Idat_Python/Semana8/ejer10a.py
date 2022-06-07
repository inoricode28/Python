from random import randint
cont=0
while True:
    cont+=1
    d1= randint(1,6)
    d2= randint(1,6)
    if d1+d2==12:
        print(d1,d2)
        break
    print(d1,d2)
print(cont)