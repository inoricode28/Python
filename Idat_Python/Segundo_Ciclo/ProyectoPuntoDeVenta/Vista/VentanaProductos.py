from PyQt5 import QtWidgets, uic
from Controlador.ArregloProductos import *
aPro = ArregloProductos()

class VentanaProductos(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaProductos, self).__init__(parent)
        uic.loadUi("UI/VentanaProductos.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnListar.clicked.connect(self.listar)
        
    
    # Métodos para obtener los valores de las cajas de texto
    # y de los combobox

    def obtenerCodigo(self):
        return self.txtCodigo.text()
    
    def obtenerNombre(self):
        return self.txtNombre.text()
    
    def obtenerDescripcion(self):
        return self.txtDescripcion.text()
    
    def obtenerMinimo(self):
        return self.txtStockMinimo.text()
    
    def obtenerActual(self):
        return self.txtStockActual.text()
    
    def obtenerCosto(self):
        return self.txtPrecioCosto.text()
    
    def obtenerPrecio(self):
        return self.txtPrecioVenta.text()
    
    def obtenerProveedor(self):
        return self.cboProveedor.currentText()
    
    def obtenerAlmacen(self):
        return self.cboAlmacen.currentText()
    
    # Método que permite limpiar la tabla

    def limpiarTabla(self):
        self.tblProductos.clearContents()
        self.tblProductos.setRowCount(0)
    
    # Método permite validar que los campos estén llenos

    def valida(self):
        if self.txtCodigo.text() == "":
            self.txtCodigo.setFocus()
            return "Código del Producto...!!!"
        if self.txtNombre.text() == "":
            self.txtNombre.setFocus()
            return "Nombre del Producto...!!!"
        if self.txtDescripcion.text() == "":
            self.txtDescripcion.setFocus()
            return "Descripción del Producto...!!!"
        if self.txtStockMinimo.text() == "":
            self.txtStockMinimo.setFocus()
            return "Stock mínimo del Producto...!!!"
        if self.txtStockActual.text() == "":
            self.txtStockActual.setFocus()
            return "Stock actual del Producto...!!!"
        if self.txtPrecioCosto.text() == "":
            self.txtPrecioCosto.setFocus()
            return "Costo del Producto...!!!"
        if self.txtPrecioVenta.text() == "":
            self.txtPrecioVenta.setFocus()
            return "Precio del Producto...!!!"
        if self.cboProveedor.currentText() == "Seleccionar Proveedor":
            self.cboProveedor.setCurrentIndex(0)
            return "Proveedor...!!!"
        if self.cboAlmacen.currentText() == "Seleccionar Almacén":
            self.cboAlmacen.setCurrentIndex(0)
            return "Almacén...!!!"
        else:
            return ""
    
    # Método que permite mostrar los datos en la tabla productos

    def listar(self):
        self.tblProductos.setRowCount(aPro.tamañoArregloProducto())
        self.tblProductos.setColumnCount(9)
        for i in range(0, aPro.tamañoArregloProducto()):
            self.tblProductos.setItem(i, 0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getCodigo()))
            self.tblProductos.setItem(i, 1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getNombre()))
            self.tblProductos.setItem(i, 2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getDescripcion()))
            self.tblProductos.setItem(i, 3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStockMinimo()))
            self.tblProductos.setItem(i, 4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStockActual()))
            self.tblProductos.setItem(i, 5, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioCosto()))
            self.tblProductos.setItem(i, 6, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioVenta()))
            self.tblProductos.setItem(i, 7, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getProveedor()))
            self.tblProductos.setItem(i, 8, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getAlmacen()))

    # Método que permite limpiar las cajas de texo y los combobox

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtNombre.clear()
        self.txtDescripcion.clear()
        self.txtStockMinimo.clear()
        self.txtStockActual.clear()
        self.txtPrecioCosto.clear()
        self.txtPrecioVenta.clear()
        self.cboProveedor.setCurrentIndex(0)
        self.cboAlmacen.setCurrentIndex(0)
    
    # Método que permite registrar los datos en la tabla

    def registrar(self):
        if self.valida() == "":
            objPro = Producto(self.obtenerCodigo(), self.obtenerNombre(), self.obtenerDescripcion(), self.obtenerMinimo(), self.obtenerActual(), self.obtenerCosto(), self.obtenerPrecio(), self.obtenerProveedor(), self.obtenerAlmacen())
            codigo = self.obtenerCodigo()
            if aPro.buscarProducto(codigo) == -1:
                aPro.adicionaProducto(objPro)
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Producto", "El código ya existe...!!!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Producto", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    # Método que permite consultar un producto
    def consultar(self):
        self.limpiarTabla()
        if aPro.tamañoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Producto", "No existen productos a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Producto", "Ingrese el código a consultar...!!!")
            pos = aPro.buscarProducto(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Producto", "El código ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.tblProductos.setRowCount(1)
                self.tblProductos.setItem(0, 0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getCodigo()))
                self.tblProductos.setItem(0, 1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getNombre()))
                self.tblProductos.setItem(0, 2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getDescripcion()))
                self.tblProductos.setItem(0, 3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getStockMinimo()))
                self.tblProductos.setItem(0, 4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getStockActual()))
                self.tblProductos.setItem(0, 5, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getPrecioCosto()))
                self.tblProductos.setItem(0, 6, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getPrecioVenta()))
                self.tblProductos.setItem(0, 7, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getProveedor()))
                self.tblProductos.setItem(0, 8, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getAlmacen()))
    #metodo que permite eliminar un producto de la lista 
    def eliminar(self):
        if aPro.tamañoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Producto", "No existen productos a eliminar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblProductos.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                codigo = self.tblProductos.item(indiceFila, 0).text()
                pos = aPro.buscarProducto(codigo)
                aPro.eliminarProducto(pos)
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto", "Debe seleccionar un fila...!!!", 
                QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aPro.tamañoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Producto", "No existen productos a modificar...!!!", 
            QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self,
             "Modificar Producto", "Ingrese el código a modificar...!!!")
            pos = aPro.buscarProducto(codigo)
            if pos != -1:
                objProducto = aPro.devolverProducto(pos)
                self.btnModificar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtCodigo.setText(objProducto.getCodigo())
                self.txtCodigo.setVisible(False)
                self.txtNombre.setText(objProducto.getNombre())
                self.txtDescripcion.setText(objProducto.getDescripcion())
                self.txtStockMinimo.setText(objProducto.getStockMinimo())
                self.txtStockActual.setText(objProducto.getStockActual())
                self.txtPrecioCosto.setText(objProducto.getPrecioCosto())
                self.txtPrecioVenta.setText(objProducto.getPrecioVenta())
                self.cboProveedor.setCurrentText(objProducto.getProveedor())
                self.cboAlmacen.setCurrentText(objProducto.getAlmacen())
    def grabar(self):
        try:
            pos = aPro.buscarProducto(self.obtenerCodigo())
            objProducto = aPro.devolverProducto(pos)
            objProducto.setNombre(self.obtenerNombre())
            objProducto.setDescripcion(self.obtenerDescripcion())
            objProducto.setStockMinimo(self.obtenerMinimo())
            objProducto.setStockActual(self.obtenerActual())
            objProducto.setPrecioCosto(self.obtenerCosto())
            objProducto.setPrecioVenta(self.obtenerPrecio())
            objProducto.setProveedor(self.obtenerProveedor())
            objProducto.setAlmacen(self.obtenerAlmacen())
            self.btnModificar.setVisible(True)
            self.btnGrabar.setVisible(True)
            self.limpiarTabla()
            self.limpiarControles()
            self.listar()
            self.txtCodigo.setVisible(True)
            self.lblCodigo.setVisible(True)      
        except:
            QtWidgets.QMessageBox.information(self, "Modificar Producto", "Error al intentar modificar...!!!", QtWidgets.QMessageBox.Ok)








       






        
        

        

        
        

