from PyQt5 import QtWidgets, uic
from Controlador.ArregloCliente import *
from Controlador.ArregloProductos import *
from Vista.VentanaCliente import *
from Vista.VentanaProductos import *


lista = []

class VentanaVentas(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaVentas, self).__init__(parent)
        uic.loadUi("UI/VentanaVentas.ui", self)
        self.btnBuscarCliente.clicked.connect(self.buscarCliente)
        self.btnBuscarProducto.clicked.connect(self.buscarProductos)
        self.btnAgregar.clicked.connect(self.agregar)
        self.Item = 0


    def buscarCliente(self):
        codigoCliente = self.txtCodigoCliente.text()
        if self.txtCodigoCliente.text() == "":
            QtWidgets.QMessageBox.information(self, "Codigo Cliente ",
            "De ingresar el codigo del cliente...!!!", QtWidgets.QMessageBox.OK)
        else:
            pos = aCli.buscarCliente(codigoCliente)
            objCliente = aCli.devolverCliente(pos)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Codigo Cliente ",
            "Cliente no registrado...!!!", QtWidgets.QMessageBox.OK)
            else:
                self.txtNombres.setText(objCliente.getNombre() + " " + objCliente.getApellidoPaterno() + " " +objCliente.getApellidoMaterno())
        

    def buscarProductos(self):
        codigoProducto = self.txtCodigoProducto.text()
        if self.txtCodigoProducto.text() == "":
            QtWidgets.QMessageBox.information(self, "Codigo Producto ",
            "De ingresar el codigo del cliente...!!!", QtWidgets.QMessageBox.OK)
        else:
            pos = aPro.buscarProducto(codigoProducto)
            objProducto = aPro.devolverProducto(pos)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Codigo Producto ",
            "Producto no registrado...!!!", QtWidgets.QMessageBox.OK)
            else:
                self.txtDescripcion.setText(objProducto.getDescripcion())
                self.txtStock.setText(objProducto.getStockActual())
                self.txtPrecio.setText(objProducto.getPrecioVenta())

    def obtenerDescripcion(self):
        return self.txtDescripcion.text()
    
    def obtenerPrecio(self):
        return float(self.txtPrecio.text(9))
    
    def obtenerCantidad(self):
        return int(self.txtCantidad.text())
    
    def obtenerItem(self):
        self.item = self.item+1
        return self.item
    
    def agregar(self):
        try:
            if self.obtenerCantidad() > int(self.txtStock.text()):
                QtWidgets.QMessageBox.information(self, "Venta", "No se puede vender esa cantidad...!!!", QtWidgets.QMessageBox.Ok)
            elif self.obtenerCantidad() <= 0:
                QtWidgets.QMessageBox.information(self, "Venta", "La cantidad ingresada es incorrecta...!!!", QtWidgets.QMessageBox.Ok)
            else:
                lista.append((self.obtenerItem(), self.obtenerCodigo(), self.obtenerDescripcion(), self.obtenerPrecio(), self.obtenerCantidad(), self.obtenerPrecio()*self.obtenerCantidad()))
                
        except:
            QtWidgets.QMessageBox.information(self, "Venta",
            "Existe un error al ingresar los productos...!!!", QtWidgets.QMessageBox.Ok)
    
    def mostrarDetalle(self):
        self.tblDetalle.setRowCount(len(lista))
        self.tblDetalle.setColumnCount(6)
        for i in range(len(lista)):
            self.tblDetalle.setItem(i, 0, QtWidgets.QTableWidgetItem(str(lista[i][0])))
            self.tblDetalle.setItem(i, 1, QtWidgets.QTableWidgetItem(str(lista[i][1])))
            self.tblDetalle.setItem(i, 2, QtWidgets.QTableWidgetItem(str(lista[i][2])))
            self.tblDetalle.setItem(i, 3, QtWidgets.QTableWidgetItem(str(lista[i][3])))
            self.tblDetalle.setItem(i, 4, QtWidgets.QTableWidgetItem(str(lista[i][4])))
            self.tblDetalle.setItem(i, 5, QtWidgets.QTableWidgetItem(str(lista[i][5])))
        self.limpiarControles()


    def limpiarControles(self):
        self.txtCodigoProducto.clear()
        self.txtDescripcion.clear()
        self.txtStock.clear()
        self.txtPrecio.clear()
        self.txtCantidad.clear()


        
