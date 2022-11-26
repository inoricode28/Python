'''
§Implementar una clase que represente una persona, que tenga como atributos codigo, nombre y edad. En el método __init__ cargar los atributos por teclado y luego ocultar cada uno de los atributos. Cree un objeto de la clase persona y usando print muestre el codigo, nombre y edad del objeto creado.
'''

class Persona:
    def __init__(self):
        self.__codigo = input("Ingrese codigo: ")
        self.__nombre = input("Ingrese nombre: ")
        self.__edad = input("Ingrese edad: ")


persona1 = Persona()
print("CODIGO: ",persona1.__codigo)
print("NOMBRE: ",persona1.__nombre)
print("EDAD: ",persona1.__edad)

