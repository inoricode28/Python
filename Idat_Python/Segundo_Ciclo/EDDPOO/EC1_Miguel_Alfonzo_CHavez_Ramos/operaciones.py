def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def producto(a,b):
    return a*b

def potenciacion(a,b):
    return a**b

def cociente (a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No es posible dividir entre cero")
        return "Operacion erronea"



