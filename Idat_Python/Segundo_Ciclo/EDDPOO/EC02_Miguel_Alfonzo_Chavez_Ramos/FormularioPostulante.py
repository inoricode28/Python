import sys
from PyQt5 import QtWidgets, uic
qtCreatorFile = "frmPostulante.ui"
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("frmPostulante.ui", self)
        
        self.btn_Aceptar.clicked.connect(self.aceptar)
        self.btn_Cerrar.clicked.connect(self.cerrar)
        self.rb_Practica.setChecked(True)
        self.rb_Desarrollo_Sistemas.setChecked(True)
        self.show()
        
        
    def aceptar(self):
        
        #Entrada de datos
        
        nombre = self.txt_Nombre.text()
        edad = self.sp_Edad.text()
        dni = self.txt_Dni.text()
     
        
        #Proceso sexo y edad
        
        if self.cbo_Sexo.currentIndex() == 1 and int(edad) <25:
            categoría = "MA"
        if self.cbo_Sexo.currentIndex() == 1 and int(edad) >=25:
            categoría = "MB"
        
        if self.cbo_Sexo.currentIndex() == 2 and int(edad) <23:
            categoría = "FA"
        if self.cbo_Sexo.currentIndex() == 2 and int(edad) >=23:
            categoría = "FB"
        
        #Proceso Modalidad
        
        if self.rb_Practica.isChecked():
            modalidad = "PR"
        
        if self.rb_Medio_Tiempo.isChecked():
            modalidad = "MT"
        
        if self.rb_Tiempo_Completo.isChecked():
            modalidad = "TC"
        
        #Proceso Área
        
        if self.rb_Desarrollo_Sistemas.isChecked():
            area = "DSI"
        
        if self.rb_Redes_Informaticas.isChecked():
            area = "RIN"
        
        if self.rb_Sorpote_Tecnico.isChecked():
            area = "STE"
        
        codigo = modalidad + area + categoría + dni
        
        #Salida de datos
        
        self.txtS.setText("Alumno: "+ nombre)
        self.txtS.append("Codigo: "+ codigo)
   
    def cerrar(self):
        self.close()
        
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()