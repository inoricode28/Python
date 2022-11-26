class Empleado:
    #constructor
    def __init__(self, codigo, nombre, dni, numH, tarifaH):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__dni = dni 
        self.__numH = numH
        self.__tarifaH = tarifaH
    
     #Métodos de acceso get y set 
    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre
    
    def getDni(self):
        return self.__dni
    
    def getNumH(self):
        return self.__numH
    
    def getTarifaH(self):
        return self.__tarifaH
    
    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setDNI(self, dni):
        self.__dni = dni
    
    def setNumH(self, numH):
        self.__numH = numH
    
    def setTarifaH(self, tarifaH):
        self.__tarifaH = tarifaH
    
    def sueldoBruto(self):
        bruto = self.getNumH() * self.getTarifaH()
        return bruto
    
    def desctESS(self):
        desctE = 0.12 * self.sueldoBruto()
        return desctE
    
    def desctAFP(self):
        desctA = 0.11 * self.sueldoBruto()
        return desctA
    
    def desctT(self):
        desctTEA = self.desctESS() + self.desctAFP()
        return desctTEA 
    
    def sueldoneto(self):
        neto = self.sueldoBruto() - self.desctT() 
        return neto
    

    

    
