'''Implemente la clase Animal, que tenga como atributos nombre,
numero_patas y tamaño. En el método __init__ cargar los atributos
por teclado y en otro método mostrar sus datos. Luego  implemente
la clase Perro y la clase Gato que hereden de la clase Animal.
Finalmente cree un objeto de las clases hijas uno para cada clase.'''

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

#LA CLASE PERRO Y LA CLASE GATO SON CLASES HIJAS O SUBCLASES

class Perro(Animal):
    pass
class Gato(Animal):
    pass

#CREAREMOS OBAJETOS DXE LA CLASE PERRO
gato1 = Gato()
gato1.mostrarDatos()

        