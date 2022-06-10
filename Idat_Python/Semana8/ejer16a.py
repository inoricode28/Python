import random
l=[]
for i in range(0,45):
    l.append(random.randint(0,20))
promedio=sum(l)/len(l)
print("notas=",l)
print("promedio=",promedio)
print("nota maxima",max(l))
print("nota minima",min(l))