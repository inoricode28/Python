import sys
from PyQt5 import QtWidgets,uic
qtCreatorFile = 'frmPrueba.ui' #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi('frmPrueba.ui',self) #ruta donde esta estar la interfas UI
        self.btnProcesar.clicked.connect(self.Procesar)
        self.btnLimpiar.clicked.connect(self.Limpiar)
        self.btnSalir.clicked.connect(self.Salir)
        self.show() #Muestra la ventana
    
    def Procesar(self):
        self.lblTexto.setText("Mi nombre es Miguel")
    def Limpiar(self):
        self.lblTexto.setText("Pulsa nuevamente en Procesar")
    def Salir(self):
        self.close()

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()