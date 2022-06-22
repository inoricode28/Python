import random
t=30
print("Nota\t","Histograma")
while(t>0):
    t-=1
    nota=random.randint(0,20)
    print(nota,"\t",'*'*nota)