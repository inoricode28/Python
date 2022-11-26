'''§Implementar una clase que represente una persona, que tenga como atributos codigo, nombre y edad. En el método __init__ cargar los atributos por teclado y luego ocultar cada uno de los atributos. Crear los métodos get y set para acceder y modificar los atributos fuera de la clase. Cree un objeto de la clase persona y usando print muestre el codigo, nombre y edad del objeto creado.'''


class Persona:
    
    # método constructor
    def __init__(self):
        self.__codigo = input("Ingrese el código: ")
        self.__nombre = input("Ingrese el nombre: ")
        self.__edad = int(input("Ingrese la edad: "))
    
    # métodos de acceso set y get
    
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def setCodigo(self, codigo):
        self.__codigo = codigo
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setEdad(self, edad):
        self.__edad = edad
    
persona1 = Persona()
print("CÓDIGO: ", persona1.getCodigo())
print("NOMBRE: ", persona1.getNombre())
print("EDAD: ", persona1.getEdad())