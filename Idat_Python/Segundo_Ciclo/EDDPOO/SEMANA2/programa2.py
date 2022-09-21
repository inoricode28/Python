try:
    a = 5
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("No se puede dividir entre 0...!!!")

except TypeError:
    print("Operacion no soportada..!!!")

except ValueError:
    print("Valores incorrectos...!!!")