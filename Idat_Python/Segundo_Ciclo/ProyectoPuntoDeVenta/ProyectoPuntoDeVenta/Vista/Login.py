from PyQt5 import QtWidgets, uic
from Vista.VentanaPrincipal import VentanaPrincipal

qtCreatorFile = "UI/Login.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Login(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        uic.loadUi("UI/Login.ui", self)

        self.btnIniciar.clicked.connect(self.iniciarSesion)
        self.show()

    def iniciarSesion(self):
        usuario = self.txtUsuario.text().lower()
        contraseña = self.txtpassword.text()
        if usuario == "mauricio" and contraseña == "123456":
            self.close()
            vprincipal = VentanaPrincipal(self)
            vprincipal.show()
        else:
            mensaje = QtWidgets.QMessageBox()
            mensaje.setWindowTitle("Punto de Venta")
            mensaje.setText("Los datos ingresado son incorrectos....")
            mensaje.setIcon(QtWidgets.QMessageBox.information)
            mensaje.exec_()
