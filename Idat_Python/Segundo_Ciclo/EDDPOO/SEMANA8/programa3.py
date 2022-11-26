class Auto:
    def inicializar(self, color, modelo, puertas, llantas, velocidades):
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
#Intancia de la clase o creaciond elos objetos
coche1 = Auto()
coche1.inicializar("Rojo","Yaris",4,4,5)
coche1.mostrarDatos()

coche2 = Auto()
coche2.inicializar("Blanco","Yaris",4,4,5)
coche2.mostrarDatos()

coche3 = Auto()
coche3.inicializar("Negro","Yaris",4,4,5)
coche3.mostrarDatos()

