from PyQt5 import QtWidgets, uic
from Controlador.ArregloCliente import ArregloClientes
from Controlador.Clientes import *

aCli = ArregloClientes()

class VentanaCliente(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaCliente, self).__init__(parent)
        uic.loadUi("UI/VentanaClientes.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnListar.clicked.connect(self.listar)

    # Métodos para obtener los valores de las cajas de texto
    # y de los combobox

    def obtenerDNI(self):
        return self.txtDni.text()

    def obtenerNombre(self):
        return self.txtNombres.text()

    def obtenerApellidoPterno(self):
        return self.txtApellidoPaterno.text()

    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()

    def obtenerDireccion(self):
        return self.txtDireccion.text()

    def obtenertelefono(self):
        return self.txtTelefono.text()

    # Método que permite limpiar la tabla

    def limpiarTabla(self):
        self.tblClientes.clearContents()
        self.tblClientes.setRowCount(0)
    
    # Método permite validar que los campos estén llenos

    def valida(self):
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI del Cliente...!!!"

        if self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombre del Cliente...!!!"

        if self.txtApellidoPaterno.text() == "":
            self.txtApellidoPaterno.setFocus()
            return "Apellido Paterno del Cliente...!!!"

        if self.txtApellidoMaterno.text() == "":
            self.txtApellidoMaterno.setFocus()
            return "Apellido Materno del Cliente...!!!"

        if self.txtDireccion.text() == "":
            self.txtDireccion.setFocus()
            return "Dirección del Cliente...!!!"

        if self.txtTelefono.text() == "":
            self.txtTelefono.setFocus()
            return "Teléfono del Cliente...!!!"

        else:
            return ""
    
    # Método que permite mostrar los datos en la tabla productos

    def listar(self):
        self.tblClientes.setRowCount(aCli.tamañoArregloCliente())
        self.tblClientes.setColumnCount(9)
        for i in range(0, aCli.tamañoArregloCliente()):
            self.tblClientes.setItem(i, 0, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDNI()))
            self.tblClientes.setItem(i, 1, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getNombre()))
            self.tblClientes.setItem(i, 2, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidoPaterno()))
            self.tblClientes.setItem(i, 3, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidoMaterno()))
            self.tblClientes.setItem(i, 4, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDireccion()))
            self.tblClientes.setItem(i, 5, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).gettelefono()))
    
    # Método que permite limpiar las cajas de texo y los combobox

    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()


# Método que permite registrar los datos en la tabla

    def registrar(self):
        if self.valida() == "":
            objCli = Cliente(self.obtenerDNI(), self.obtenerNombre(), self.obtenerApellidoPterno(), self.obtenerApellidoMaterno(), self.obtenerDireccion(), self.obtenertelefono())
            Dni = self.obtenerDNI()

            if aCli.buscarCliente(Dni) == -1:
                aCli.adicionaCliente(objCli)
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente", "El Dni ya existe...!!!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    # Método que permite consultar un Cliente

    def consultar(self):
        self.limpiarTabla()
        if aCli.tamañoArregloCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Clientes", "No existen Clientes a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Clientes", "Ingrese el DNI a consultar...!!!")
            pos = aCli.buscarCliente(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Cliente", "El DNI ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.tblClientes.setRowCount(1)
                self.tblClientes.setItem(0, 0, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getDNI()))
                self.tblClientes.setItem(0, 1, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getNombre()))
                self.tblClientes.setItem(0, 2, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getApellidoPaterno()))
                self.tblClientes.setItem(0, 3, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getApellidoMaterno()))
                self.tblClientes.setItem(0, 4, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getDireccion()))
                self.tblClientes.setItem(0, 5, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).gettelefono()))
                      
 # Método que permite eliminar un Cliente de la lista



    def eliminar(self):

        if aCli.tamañoArregloCliente() == 0:

            QtWidgets.QMessageBox.information(self, "Eliminar Clientes", "No existen pClientes a eliminar...!!!", QtWidgets.QMessageBox.Ok)

        else:

            fila = self.tblClientes.selectedItems()

            if fila:

                indiceFila = fila[0].row()

                Dni = self.tblClientes.item(indiceFila, 0).text()

                pos = aCli.buscarCliente(Dni)

                aCli.eliminarCliente(pos)

                self.limpiarTabla()

                self.listar()

            else:

                QtWidgets.QMessageBox.information(self, "Eliminar Clientes", "Debe seleccionar un fila...!!!", QtWidgets.QMessageBox.Ok)    
            



    

