# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ELPAPI\Desktop\ProyectoPuntoDeVenta\UI\VentanaClientes.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 641)
        MainWindow.setStyleSheet("background-color: rgb(15, 125, 209);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 10, 161, 51))
        self.label.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.txtDni = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDni.setGeometry(QtCore.QRect(10, 80, 301, 20))
        self.txtDni.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDni.setObjectName("txtDni")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 91, 41))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.txtNombres = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombres.setGeometry(QtCore.QRect(10, 140, 301, 20))
        self.txtNombres.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtNombres.setObjectName("txtNombres")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 100, 141, 41))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.txtApellidoPaterno = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellidoPaterno.setGeometry(QtCore.QRect(320, 140, 301, 20))
        self.txtApellidoPaterno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtApellidoPaterno.setObjectName("txtApellidoPaterno")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(630, 100, 141, 41))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.txtApellidoMaterno = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellidoMaterno.setGeometry(QtCore.QRect(630, 140, 311, 20))
        self.txtApellidoMaterno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtApellidoMaterno.setObjectName("txtApellidoMaterno")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 91, 21))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.txtDireccion = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDireccion.setGeometry(QtCore.QRect(10, 200, 611, 20))
        self.txtDireccion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDireccion.setObjectName("txtDireccion")
        self.txtTelefono = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelefono.setGeometry(QtCore.QRect(630, 200, 311, 20))
        self.txtTelefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtTelefono.setObjectName("txtTelefono")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(630, 160, 141, 41))
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.tblClientes = QtWidgets.QTableWidget(self.centralwidget)
        self.tblClientes.setGeometry(QtCore.QRect(10, 230, 931, 291))
        self.tblClientes.setAcceptDrops(False)
        self.tblClientes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tblClientes.setObjectName("tblClientes")
        self.tblClientes.setColumnCount(6)
        self.tblClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Apellido Paterno")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(5, item)
        self.btnRegistrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrar.setGeometry(QtCore.QRect(10, 540, 171, 51))
        self.btnRegistrar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(235, 38, 12);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\ELPAPI\\Desktop\\ProyectoPuntoDeVenta\\UI\\../IMG/registrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRegistrar.setIcon(icon)
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.btnModificar = QtWidgets.QPushButton(self.centralwidget)
        self.btnModificar.setGeometry(QtCore.QRect(200, 540, 171, 51))
        self.btnModificar.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(235, 38, 12);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\ELPAPI\\Desktop\\ProyectoPuntoDeVenta\\UI\\../IMG/modificar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon1)
        self.btnModificar.setObjectName("btnModificar")
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(390, 540, 171, 51))
        self.btnConsultar.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(235, 38, 12);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\ELPAPI\\Desktop\\ProyectoPuntoDeVenta\\UI\\../IMG/consultar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConsultar.setIcon(icon2)
        self.btnConsultar.setObjectName("btnConsultar")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(580, 540, 171, 51))
        self.btnEliminar.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(235, 38, 12);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\ELPAPI\\Desktop\\ProyectoPuntoDeVenta\\UI\\../IMG/eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon3)
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnListar = QtWidgets.QPushButton(self.centralwidget)
        self.btnListar.setGeometry(QtCore.QRect(770, 540, 171, 51))
        self.btnListar.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(235, 38, 12);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\ELPAPI\\Desktop\\ProyectoPuntoDeVenta\\UI\\../IMG/listar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListar.setIcon(icon4)
        self.btnListar.setObjectName("btnListar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 953, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CLIENTES"))
        self.label_2.setText(_translate("MainWindow", "DNI:"))
        self.label_3.setText(_translate("MainWindow", "Nombres:"))
        self.label_4.setText(_translate("MainWindow", "Apellido Paterno:"))
        self.label_5.setText(_translate("MainWindow", "Apellido Materno:"))
        self.label_6.setText(_translate("MainWindow", "Dirección:"))
        self.label_7.setText(_translate("MainWindow", "Teléfono:"))
        item = self.tblClientes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.tblClientes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombres"))
        item = self.tblClientes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Apellido Materno "))
        item = self.tblClientes.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Dirección"))
        item = self.tblClientes.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Teléfono"))
        self.btnRegistrar.setText(_translate("MainWindow", "Registrar"))
        self.btnModificar.setText(_translate("MainWindow", "Modificar"))
        self.btnConsultar.setText(_translate("MainWindow", "Consultar"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.btnListar.setText(_translate("MainWindow", "Listar"))
