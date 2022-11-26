class Auto:    
    #Atributos
    color = ""
    modelo = ""
    puerta = 0 
    llantas = 0
    velocidades = 0 
    
    #Metodos
    def mostrarDatos(self):
        print("COLOR: ", self.color)
        print("MODELO: ", self.modelo)
        print("PUERTAS: ", self.puerta)
        print("LLANTAS: ", self.llantas)
        print("VELOCIDADES: ", self.velocidades)
    
# instanciamos la clase
# Creacion de objetos
coche1 = Auto()
coche1.color = "Azul"
coche1.modelo = "Yaris"
coche1.puerta = 4
coche1.llantas = 4
coche1.velocidades = 5
coche1.mostrarDatos()

coche2 = Auto()
coche2.color = "rojo"
coche2.modelo = "Yaris"
coche2.puerta = 4
coche2.llantas = 4
coche2.velocidades = 5
coche2.mostrarDatos()
        
coche3 = Auto()
coche3.color = "Blanco"
coche3.modelo = "Yaris"
coche3.puerta = 4
coche3.llantas = 4
coche3.velocidades = 5
coche3.mostrarDatos()

coche4 = Auto()
coche4.color = "Negro Fantasma"
coche4.modelo = "Yaris"
coche4.puerta = 4
coche4.llantas = 4
coche4.velocidades = 5
coche4.mostrarDatos()

coche5 = Auto()
coche5.color = "Gris"
coche5.modelo = "Yaris"
coche5.puerta = 4
coche5.llantas = 4
coche5.velocidades = 5
coche5.mostrarDatos()
