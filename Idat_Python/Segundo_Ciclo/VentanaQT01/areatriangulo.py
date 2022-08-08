import sys
from PyQt5 import QtWidgets,uic

qtCreatorFile = "frmAreaTriangulo.ui" #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("frmAreaTriangulo.ui",self) #ruta donde esta estar la interfas UI
        self.btnSalir.clicked.connect(self.salir)
        self.btnCalcular.clicked.connect(self.calcular)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.show() #Muestra la ventana

    def calcular(self):
        #Entrada de datos
        base = float(self.txtBase.text())
        altura = float(self.txtAltura.text())
        #Proceso de datos 
        area = (base*altura)/2   
        #Salida de resultados
        self.txtS.setText("AREA DEL TRIANGULO: \n")
        self.txtS.append("El valor de la base es: "+str(base))
        self.txtS.append("El valor de la Altura es: "+str(altura))
        self.txtS.append("El valor de la area es: "+str(area))

    def limpiar(self):
        self.txtBase.setText("")
        self.txtAltura.setText("")
        self.txtS.setText("")
        
    def salir(self):
        self.close()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()
