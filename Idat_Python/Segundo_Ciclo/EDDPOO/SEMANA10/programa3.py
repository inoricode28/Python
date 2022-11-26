'''
§Implementar una clase Persona que tenga dos atributos: nombre y edad.
Definir dos métodos para la carga por teclado y su impresión.
Implementar una segunda clase llamada Empleado que herede de la
clase Persona y agregue un atributo sueldo y muestre si debe pagar
impuestos (sueldo superior a 2500). Crear un objeto de cada clase.
'''

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

    def mostrarDatos(self):
        print("NOMBRE: ", self.nombre)
        print("NOMBRE: ", self.edad)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo: "))

    def mostrarDatos(self):
        super().mostrarDatos()
        print("SUELDO: ", self.sueldo)

    def pagaImpuestos(self):
        if self.sueldo > 2500:
            print("SI paga impuestos...!!!")
        else:
            print("NO paga impuestos...!!!")
    
Persona1 = Persona()
Persona1.mostrarDatos()
print("==========================")
empleado1 = Empleado()
empleado1.mostrarDatos()
empleado1.pagaImpuestos()



