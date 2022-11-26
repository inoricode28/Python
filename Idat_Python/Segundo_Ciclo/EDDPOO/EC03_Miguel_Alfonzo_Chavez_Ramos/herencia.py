class Entidad:
    def __init__(self,razon_social,ruc):
        self.__razon_social=razon_social
        self.__ruc=ruc
    def getRazonSocial(self):
        return self.__razon_social
    def getRUC(self):
        return self.__ruc
    def setRazonSocial(self,razon_social):
        self.__razon_social=razon_social
    def setRUC(self,ruc):
        self.__ruc=ruc
    def mostrarDatos(self):
        print("Razón Social\t\t:",self.getRazonSocial())
        print("RUC\t\t\t:",self.getRUC())

class Banco(Entidad):
    def __init__(self,razon_social,ruc,deposito,interes_anual):
        super().__init__(razon_social,ruc)
        self.deposito=deposito
        self.interes_anual=interes_anual
    def mostrarDatos(self):
        print("+---------+\nCLASE BANCO\n+---------+")
        super().mostrarDatos()
        print("Depósito\t\t: S/.",self.deposito)       
        print("Interés Anual\t\t:",self.interes_anual,"%")
   
    def calcularSaldo(self):
        saldo=(self.deposito+self.deposito*self.interes_anual/100)
        return print("SALDO\t\t\t: S/.",saldo,"\n")
    
class Financiera (Entidad):
    def __init__(self,razon_social,ruc,prestamo,cobro_por_operacion):
        super().__init__(razon_social,ruc)
        self.prestamo=prestamo
        self.cobro_por_operacion=cobro_por_operacion
    def mostrarDatos(self):
        print("+--------------+\nCLASE FINANCIERA\n+--------------+")
        super().mostrarDatos()
        print("Préstamo\t\t: S/.",self.prestamo)
        print("Cobro por operación\t: S/.",self.cobro_por_operacion)
    def calcularPrestamo(self):
        prestamo=self.prestamo-self.cobro_por_operacion
        return print("Monto de préstamo\t: S/.",prestamo)

banco1=Banco("Miguel Chavez", 10422292743, 5000, 20)
banco1.mostrarDatos()
banco1.calcularSaldo()

financiera1=Financiera("Jose Ramos", 14101115017, 5000, 100)
financiera1.mostrarDatos()
financiera1.calcularPrestamo()