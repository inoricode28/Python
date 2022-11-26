import sys
from PyQt5 import QtWidgets,uic
from claseAlumno import Alumno

qtCreatorFile = 'SEMANA10/PaqueteAlumno2/frmAlumno.ui' #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class FormularioAlumno(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(FormularioAlumno, self).__init__(parent)
        uic.loadUi('SEMANA10/PaqueteAlumno2/frmAlumno.ui',self) #ruta donde esta estar la interfas UI
        self.btnProcesar.clicked.connect(self.procesar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        self.show() #Muestra la ventana
    
    def procesar(self):
        alumno1 = Alumno("Kenny",17,18)
        self.mostrarDatos(alumno1)

        alumno2 = Alumno("Miguel",17,18)
        self.mostrarDatos(alumno2)

        alumno3 = Alumno("Jose",17,18)
        self.mostrarDatos(alumno3)

        alumno4 = Alumno("Coty",17,18)
        self.mostrarDatos(alumno4)

    def imprimir(self,cad):
        self.txtS.append(cad)
    
    def mostrarDatos(self,Alumno):
        self.imprimir("Nombre\t: " + str(Alumno.getNombre()))
        self.imprimir("Nota1\t: " + str(Alumno.getNota1()))
        self.imprimir("Nota2\t: " + str(Alumno.getNota2()))
        self.imprimir("Promedio\t: " + str(Alumno.promedio()))


    def limpiar(self):
        self.txtS.setText("")
    
    def salir(self):
        self.close()

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioAlumno()
    app.exec()