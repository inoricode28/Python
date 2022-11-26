import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = "frmRegistroVentas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

lista = []

class Formulario(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("frmRegistroVentas.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnNuevo.clicked.connect(self.nuevo)
        self.btnSalir.clicked.connect(self.salir)
        self.show()
    
    def registrar(self):
        
        # Entrada de datos
        producto = self.cboProducto.currentText()
        tipoPago = self.cboPago.currentText()
        cantidad = int(self.txtCantidad.text())
        
        # Mostrarmos el precio del producto
        precio = 0
        if producto == "Colección Escolar": 
            precio = 240
        if producto == "Colección PreUniversitaria":
            precio = 150
        if producto == "Colección Profesional":
            precio = 350
            
        self.lblPrecio.setText("S/. " + str(precio))
        
        # Calculamos el subtotal
        subtotal = precio * cantidad
        
        # Calculamos el descuento y el recargo
        descuento = 0
        recargo = 0
        if tipoPago == "Contado":
            descuento = 0.05 * subtotal
        if tipoPago == "Tarjeta":
            recargo = 0.10 * subtotal
        
        # Calculamos el precio final
        precioFinal = subtotal - descuento + recargo
        
        datos = (producto, str(cantidad), "S/. " + str(precio), tipoPago, "S/. " + str(descuento), "S/. " + str(recargo), "S/. " + str(precioFinal))
        lista.append(datos)
        self.listar()
    
    def listar(self):
        self.tblDatos.setRowCount(50)
        for i in range(len(lista)):
            self.tblDatos.setItem(i, 0, QtWidgets.QTableWidgetItem(lista[i][0]))
            self.tblDatos.setItem(i, 1, QtWidgets.QTableWidgetItem(lista[i][1]))
            self.tblDatos.setItem(i, 2, QtWidgets.QTableWidgetItem(lista[i][2]))
            self.tblDatos.setItem(i, 3, QtWidgets.QTableWidgetItem(lista[i][3]))
            self.tblDatos.setItem(i, 4, QtWidgets.QTableWidgetItem(lista[i][4]))
            self.tblDatos.setItem(i, 5, QtWidgets.QTableWidgetItem(lista[i][5]))
            self.tblDatos.setItem(i, 6, QtWidgets.QTableWidgetItem(lista[i][6]))
            
    
    def nuevo(self):
        pass
    
    def salir(self):
        self.close()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()