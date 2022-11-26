import sys
from PyQt5 import QtWidgets,uic
qtCreatorFile = 'frmAreaTriangulo.ui' #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi('frmAreaTriangulo.ui',self) #ruta donde esta estar la interfas UI
        self.btnCalcular.clicked.connect(self.Calcular)
        self.btnLimpiar.clicked.connect(self.Limpiar)
        self.btnSalir.clicked.connect(self.Salir)
        self.show() #Muestra la ventana
    
    def Calcular(self):
        #Entrada de datos
        base = float(self.txtBase.text())
        altura = float(self.txtAltura.text())

        #Proceso de calculo
        area = (base*altura) / 2
        #Salida de resultado
        self.txtS.setText("AREA DEL TRIANGULO:\n")
        self.txtS.append("El valor de la base es: " + str(base))
        self.txtS.append("El valor de la altura es: " + str(altura))
        self.txtS.append("El valor del area es: " + str(area))

    def Limpiar(self):
        self.txtBase.setText("")
        self.txtAltura.setText("")
        self.txtS.setText("")
    def Salir(self):
        self.close()

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()