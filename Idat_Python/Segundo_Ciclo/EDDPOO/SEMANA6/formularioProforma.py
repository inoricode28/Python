from code import interact
import sys
from PyQt5 import QtWidgets,uic
qtCreatorFile = 'SEMANA6/frmProforma.ui' #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi('SEMANA6/frmProforma.ui',self) #ruta donde esta estar la interfas UI
        self.btnCalcular.clicked.connect(self.calcular)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        #self.rbInteres1.setChecked(True)
        #self.rbMayorista.setChecked(True)
        self.show() #Muestra la ventana

    def calcular(self):
        #Entrda de datos
        precio = float(self.txtPrecio.text())
        cantidad = int(self.spbCantidad.value())

        #Proceso de calculo
        importe = precio*cantidad

        porcentajeDescuento = 0

        if self.rbMayorista.isChecked() == True:
            porcentajeDescuento = 4.5/100
        if self.rbMinorista.isChecked()==True:
            porcentajeDescuento = 1.9/100

        descuento = importe * porcentajeDescuento
        
        porcentajeInteres = 0
        if self.rbInteres1.isChecked() == True:
            porcentajeInteres = 0/100
        if self.rbInteres2.isChecked() == True:
            porcentajeInteres = 8.5/100
        if self.rbInteres3.isChecked() == True:
            porcentajeInteres = 12.5/100
        
        interes = importe * porcentajeInteres
        total = importe - descuento + interes

        #Salida de resultados
        self.txtImporte.setText("S/." + "{:.2f}".format(importe))
        self.txtDescuento.setText("S/." + "{:.2f}".format(descuento))
        self.txtInteres.setText("S/." + "{:.2f}".format(interes))
        self.txtTotal.setText("S/." + "{:.2f}".format(total))
        self.txtS.setText("= = = = = = = = = = = = = = = =".center(80))
        self.txtS.append("|   P  R  O  F  O  R  M  A |".center(90))
        self.txtS.append("= = = = = = = = = = = = = = = =".center(80))
        self.txtS.append("CÓDIGO DEL CLIENTE\t: " + self.txtCodigoCliente.text())
        self.txtS.append("NOMBRE DEL CLIENTE\t: " + self.txtNombreCliente.text()+"\n")
        self.txtS.append("PRODUCTO\t\t: " + self.txtProducto.text())
        self.txtS.append("CANTIDAD\t\t" + "{:.2f}".format(cantidad))
        self.txtS.append("El importe de la compra es\t" + "{:.2f}".format(importe))
        self.txtS.append("El descuento de la compra es\t" + "{:.2f}".format(descuento))
        self.txtS.append("El interes de la compra es\t" + "{:.2f}".format(interes))
        self.txtS.append("El total a pagar es\t" + "{:.2f}".format(total))



        
    def limpiar(self):
        self.txtCodigoCliente.setText("")
        self.txtNombreCliente.clear()
        self.spbCantidad.setValue(0)
        self.rbInteres1.setChecked(True)
        self.rbMayorista.setChecked(True)
        self.txtProducto.setText("")
        self.txtPrecio.setText("")
        self.txtImporte.setText("")
        self.txtDescuento.setText("")
        self.txtInteres.setText("")
        self.txtTotal.setText("")
        self.txtS.setText("")
    def salir(self):
        self.close()
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()