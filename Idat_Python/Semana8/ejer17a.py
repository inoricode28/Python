from random import randint
cont=0
more=0
while cont<=200:
    cont+=1
    n=randint(100,999)
    unidades=n%10
    centenas= n//100
    if unidades==centenas:
        more+=1
        print(n,"Capicua")
    else:
        print(n,"No capicua")
print(more,"Son Capicua")
print(200-more,"No son Capicua")