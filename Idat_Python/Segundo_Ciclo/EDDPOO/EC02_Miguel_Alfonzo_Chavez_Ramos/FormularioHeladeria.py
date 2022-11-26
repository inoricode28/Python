import sys
from PyQt5 import QtWidgets,uic
qtCreatorFile = 'frmHeladeria.ui' 
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi('frmHeladeria.ui' ,self) 
        
        self.btn_Procesar.clicked.connect(self.procesar)
        self.btn_Borrar.clicked.connect(self.borrar)
        self.btn_Salir.clicked.connect(self.salir)
        self.rbFrio_Rico.setChecked(True)
        self.show() 

    def procesar(self):
        #Entrada de datos        
        cantidad = int(self.txt_Cantidad.text())
        precio = 0
        
        #Proceso      
        
        if self.rbFrio_Rico.isChecked():
            precio = 1.50
        if self.rbBonbones.isChecked():
            precio = 2.50
        if self.rb_Sandwich.isChecked():
            precio = 3.50
        if self.rb_Dolceto.isChecked():
            precio = 4.50
            
        total = cantidad * precio
             
        #Salida de datos        
        self.txtS.setText("Cantidad a comprar: " + self.txt_Cantidad.text())
        self.txtS.append("Monto a pagar: S/. " + str(total) +"\n")
        self.txtS.append("Gracias por usar el programa...!!!")

    def borrar(self):
  
        self.txt_Cantidad.setText("")
        self.rbFrio_Rico.setChecked(True)
        self.txtS.setText("")    

    def salir(self):
        self.close()

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()