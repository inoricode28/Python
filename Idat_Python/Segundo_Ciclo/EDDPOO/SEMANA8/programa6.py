class Auto:
    #El metodo __init__ es el metodo contrsuctor
    #(es el que contruye la clase)
    def __init__(self,color, modelo, puertas, llantas, velocidades):
        self.color = color
        self.modelo = modelo
        self.puertas = puertas
        self.llantas = llantas
        self.velocidades = velocidades

    def mostrarDatos(self):
        print("COLOR: ", self.color)
        print("MODELO: ", self.modelo)
        print("PUERTAS: ", self.puertas)
        print("LLANTAS: ", self.llantas)
        print("VELOCIDADES: ", self.velocidades)   

#instanaciamos la clase o creamos los objetos 
coche1 = Auto("rojo","Yaris",4,4,5)
coche1.mostrarDatos()
