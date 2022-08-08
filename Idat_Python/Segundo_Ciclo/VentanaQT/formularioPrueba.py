import sys
from PyQt5 import QtWidgets,uic

qtCreatorFile = "frmPrueba.ui"
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("frmPrueba.ui",self)
        self.btnsalir.clicked.connect(self.salir)
        self.btnprocesar.clicked.connect(self.procesar)
        self.btnlimpiar.clicked.connect(self.limpiar)
        self.show()
    
    
    def procesar(self):
        self.lbltexto.setText("Hola a todos...!!!")
    def limpiar(self):
        self.lbltexto.setText("Pulsa otra vez...!!!")
    def salir(self):
        self.close()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()
