class PC:
    #El metodo __init__ es el metodo contrsuctor
    #(es el que contruye la clase)
    def __init__(self,memoria, HDD, Placa, Teclado, Pantalla):
        self.memoria = memoria
        self.HDD = HDD
        self.Placa = Placa
        self.Teclado = Teclado
        self.Pantalla = Pantalla

    def mostrarDatos(self):
        print("memoria: ", self.memoria)
        print("HDD: ", self.HDD)
        print("Placa: ", self.Placa)
        print("Teclado: ", self.Teclado)
        print("Pantalla: ", self.Pantalla)   

#instanaciamos la clase o creamos los objetos 
coche1 = PC("DDR3","SEAGATE",915,"KG512","LG")
coche1.mostrarDatos()
