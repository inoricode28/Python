class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("NOMBRE: ",self.nombre)
        print("NOTA: ",self.nota)
        self.condicion()
    

    def condicion(self):
        if self.nota >= 13:
            print("APROBADOO...!!!!")
        else:
            print("DESAPROBADO...!!!!")

#instanciamos la clase o creamos los objetos
alumno1 = Alumno("Miguel",20)
alumno1.imprimir()


