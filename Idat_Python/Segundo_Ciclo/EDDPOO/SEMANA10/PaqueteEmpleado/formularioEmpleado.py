import sys
from PyQt5 import QtWidgets,uic
from claseEmpleado import Empleado

qtCreatorFile = 'SEMANA10/PaqueteEmpleado/frmEmpleado.ui' #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi('SEMANA10/PaqueteEmpleado/frmEmpleado.ui',self) #ruta donde esta estar la interfas UI
        self.btnProcesar.clicked.connect(self.procesar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        self.show() #Muestra la ventana
    
    def procesar(self):
        empleado1 = Empleado(1,"Kenny",40,150.0)
        self.mostrarDatos(empleado1)

    
    def imprimir(self,cad):
        self.txtS.append(cad)

    def mostrarDatos(self,Empleado):
        self.imprimir("CODIGO"+str(Empleado.getCodigo()))
        self.imprimir("NOMBRE: "+str(Empleado.getNombre()))
        self.imprimir("HORAS: "+str(Empleado.getHoras()))
        self.imprimir("TARIFA: S/."+str(Empleado.getHoras()))
        self.imprimir("SUELDO BRUTO: S/."+str(Empleado.sueldoBruto()))
        self.imprimir("DESCUENTO: "+str(Empleado.descuento()))
        self.imprimir("SUELDO NETO: S/."+str(Empleado.sueldoNeto()))


    def limpiar(self):
        self.txtS.setText("")

    def salir(self):
        self.close()

    

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()