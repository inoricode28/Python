nota=int(input('Ingrese nota: '))
if nota<0 or nota>20:
    nota =-1
if nota>=11:
    nota+=2
if nota>20:
    nota=20

if nota==-1:
    print("Nota no valida")

if nota!=-1:
    print("Nota final",nota)