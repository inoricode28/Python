class Auto:
    #El metodo __init__ es el metodo contrsuctor
    #(es el que contruye la clase)
    def __init__(self):
        self.color = input("Ingrese el color: ")
        self.modelo = input("Ingrese el modelo: ")
        self.puertas = int(input("Ingrese las puertas: "))
        self.llantas = int(input("Ingrese las llantas: "))
        self.velocidades = int(input("Ingrese las velocidades: "))

    def mostrarDatos(self):
        print("COLOR: ", self.color)
        print("MODELO: ", self.modelo)
        print("PUERTAS: ", self.puertas)
        print("LLANTAS: ", self.llantas)
        print("VELOCIDADES: ", self.velocidades)   

#instanaciamos la clase o creamos los objetos 
coche1 = Auto()
coche1.inicializar()
coche1.mostrarDatos()

coche2 = Auto()
coche2.inicializar()
coche2.mostrarDatos()

coche3 = Auto()
coche3.inicializar()
coche3.mostrarDatos()

coche4 = Auto()
coche4.inicializar()
coche4.mostrarDatos()

coche5 = Auto()
coche5.inicializar()
coche5.mostrarDatos()