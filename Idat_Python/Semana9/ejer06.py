#Diseñe un programa que imprima y sume 20 términos de la siguiente serie:
#7, 9, 13, 15, 20, 22, ...
#2-4-2-5-2-6-2-7

termino=7
razonImpar=2
razonPar=4

for i in range(1,21):
    print(termino,end=" ")
    if i%2==0:
        termino+=razonPar
        razonPar+=1
    else:
        termino+=razonImpar



