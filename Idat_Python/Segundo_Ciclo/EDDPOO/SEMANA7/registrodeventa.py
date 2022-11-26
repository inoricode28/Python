import sys
from PyQt5 import QtWidgets,uic
qtCreatorFile = 'registrodeventa.ui' #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
lista = []
class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi('registrodeventa.ui',self) #ruta donde esta estar la interfas UI
        self.btnRegistrar.clicked.connect(self.registrar) 
        self.btnNuevo.clicked.connect(self.nuevo)
        self.btnSalir.clicked.connect(self.salir)
        self.btnlimpiarTabla.clicked.connect(self.limpiarTabla) 
        self.show() #Muestra la ventana
    
    def registrar(self):

        # Entrada de datos 
        dia = self.dtFecha.date().day() 
        mes = self.dtFecha.date().month() 
        año = self.dtFecha.date().year() 
        fecha = str(dia) + "/" + str(mes) + "/" + str(año)   
 
        producto = self.cboProducto.currentText()  #Obtener el texto del Combo box 
        tipoPago = self.cboPago.currentText() 
        cantidad = int(self.txtCantidad.text())
        
        # Mostrar el precio del producto 
        precio = 0 
        if producto == "Colección Escolar":               
            precio = 240 
        if producto == "Colección PreUniversitaria": 
            precio = 150 
        if producto == "Colección Profesional": 
            precio = 350
        
        # Mostrar el precio del producto en la etiqueta 
        self.lblPrecio.setText("S/. " + str(precio))      
 
        # Calculamos el subtotal 
        subTotal = precio * cantidad

        # Calculamos el descuento y el recargo 
        descuento = 0 
        recargo = 0 
        if tipoPago == "Contado": 
            descuento = 0.05 * subTotal 
        if tipoPago == "Tarjeta": 
            recargo = 0.1 * subTotal 
 
        # Calculamos el precio final 
        precioFinal = subTotal - descuento + recargo

        #Agregando datos a la lista para mostrar en la tabla 
        datos = (producto, str(cantidad), str(precio), str(tipoPago), str(descuento), str(recargo), str(precioFinal), fecha) 
        lista.append(datos) 
        self.listar()
    
    def listar(self):        # Listado de datos 
        self.tblDatos.setRowCount(50) 
        #self.tblDatos.verticalHeader().setVisible(False)  #Para que no salgan nmrs en la columna verticar 
        for i in range (0, len(lista)): 
            #self.tblDatos.setItem(i, 0, QtWidgets.QTableWidgetItem(lista[i][0])) 
            self.tblDatos.setItem(i, 1, QtWidgets.QTableWidgetItem(lista[i][1])) 
            self.tblDatos.setItem(i, 2, QtWidgets.QTableWidgetItem(lista[i][2])) 
            self.tblDatos.setItem(i, 3, QtWidgets.QTableWidgetItem(lista[i][3])) 
            self.tblDatos.setItem(i, 4, QtWidgets.QTableWidgetItem(lista[i][4])) 
            self.tblDatos.setItem(i, 5, QtWidgets.QTableWidgetItem(lista[i][5])) 
            self.tblDatos.setItem(i, 6, QtWidgets.QTableWidgetItem(lista[i][6])) 
            self.tblDatos.setItem(i, 7, QtWidgets.QTableWidgetItem(lista[i][7]))

    def limpiarTabla(self):
        self.tblDatos.clearContents()    # Agregar otro boton para limpiar la tabla
        self.tblDatos.setRowCount(0) 
 
    def nuevo(self): 
        self.txtCantidad.clear() 
        self.lblPrecio.clear() 
        self.cboProducto.setCurrentIndex(0) 
        self.cboPago.setCurrentIndex(0) 
 
 
    def salir(self): 
        self.close()



if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()