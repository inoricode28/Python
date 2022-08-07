def area(a,b):    
    if a>b:
        return b,"Menor"        
    elif b>a:
        return a,"Menor"       
    elif a==b:
        return "Son iguales"      

print(area(5,6))