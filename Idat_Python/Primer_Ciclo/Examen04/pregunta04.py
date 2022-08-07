def diccionario(tupla):
    lista_a=[]
    lista_b=list(tupla)
    lista_c=[]
    for i in range(len(lista_b)):
        lista_a.append(lista_b[i])
        lista_c.append(lista_b.count(lista_b[i]))
    return dict(zip(lista_a,lista_c))
tupla=("a", "b", "c", "a", "d", "b", "a", "e", "d", "e", "a", "e")
diccionario_tot=diccionario(tupla)

#RESULTADO
print(diccionario_tot)