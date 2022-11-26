import sys
from PyQt5 import QtWidgets, uic
from claseEmpleado import Empleado

qtCreatorFile = "PaqueteEmpleado/frmEmpleado.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class FormularioEmpleado(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(FormularioEmpleado, self).__init__(parent)
        uic.loadUi("PaqueteEmpleado/frmEmpleado.ui", self)
        #Aqui van los botones que se estan en el formulario QT
        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCerrar.clicked.connect(self.cerrar)
    
        self.show()
    
    def aceptar(self):
        Empleado1 = Empleado("C0001", "MIGUEL", 42229274, 10, 20)
        self.mostrarDatos(Empleado1)
    
    def imprimir(self,cadena):
        self.txtS.append(cadena)
    

    
    def mostrarDatos(self, Empleado):
        self.imprimir("CÓDIGO\t\t:"+ str(Empleado.getCodigo()))
        self.imprimir("NOMBRE\t\t:"+ str(Empleado.getNombre()))
        self.imprimir("DNI\t\t:"+ str(Empleado.getDni()))
        self.imprimir("\nNÚMERO DE HORAS\t:"+ str(Empleado.getNumH()))
        self.imprimir("TARIFA POR HORA\t:S/. "+ str("{:.2f}".format(Empleado.getTarifaH()))) 
        self.imprimir("SUELDO BRUTO\t\t:S/. "+ str("{:.2f}".format(Empleado.sueldoBruto())))
        self.imprimir("DESCUENTO ESSALUD(12%)\t:S/. "+ str("{:.2f}".format(Empleado.desctESS())))
        self.imprimir("DESCUENTO AFP(11%)\t:S/. "+ str("{:.2f}".format(Empleado.desctAFP())))
        self.imprimir("DESCUENTO TOTAL\t:S/. "+ str("{:.2f}".format(Empleado.desctT())))
        self.imprimir("SUELDO NETO\t\t:S/. "+ str("{:.2f}".format(Empleado.sueldoneto())))
    
    def cerrar(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioEmpleado()
    app.exec() 






        




    

        




