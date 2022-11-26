class Empleado:

    #contructor
    def __init__(self, codigo, nombre, horas, tarifa):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__horas = horas
        self.__tarifa = tarifa
    
    #metodos get y set
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getHoras(self):
        return self.__horas
    
    def getTArifa(self):
        return self.__tarifa
    
    def setCodigo(self, codigo):
        self.__horas = codigo
    
    def setNombre(self, nombre):
        self.__horas = nombre
    
    def setHoras(self, horas):
        self.__horas = horas
    
    def setTarifa(self, tarifa):
        self.__horas = tarifa
    
    #metodo de calculo

    def sueldoBruto(self):
        return self.getHoras() * self.getTArifa()

    def descuento(self):
        return self.sueldoBruto() * 0.11
    def sueldoNeto(self):
        return self.sueldoBruto() - self.descuento()
    