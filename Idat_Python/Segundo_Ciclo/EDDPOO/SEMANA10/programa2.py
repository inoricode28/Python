'''Implemente la clase Animal, que tenga como atributos nombre,
numero_patas y tamaño. En el método __init__ cargar los atributos
por teclado y en otro método mostrar sus datos. Luego  implemente
la clase Canino que tiene como atributo raza y la clase Perro que
tiene como atributo numero_vacunas, la clase Canino hereda de la
clase Animal y la clase Perro hereda de la clase Canino. Finalmente
cree dos objetos de la clase Perro.'''

class Animal:
    #Contructor
    def __init__(self):
        self.nombre = input("Ingrese nombre: ")
        self.numero_patas = input("Ingrese el numero de patas: ")
        self.tamaño = input("Ingrese el tamaño: ")

    #Métodos
    def mostrarDatos(self):
        print("NOMBRE: ",self.nombre)
        print("NUMERO DE PATAS",self.numero_patas)
        print("TAMAÑO: ",self.tamaño)

class Canino(Animal):
    def __init__(self):
        super().__init__()
        self.raza = input("Ingrese la raza: ")
    
    def mostrarDatos(self):
        super().mostrarDatos()
        print("RAZA: ", self.raza)

class Perro(Canino):
    def __init__(self):
        super().__init__()
        self.numero_vacunas = int(input("Ingrese el numero de vacunas: "))
    
    def mostrarDatos(self):
        super().mostrarDatos()
        print("VACUNAS: ",self.numero_vacunas)

#Creacion de objetos
perro1 = Perro()
perro1.mostrarDatos() 

