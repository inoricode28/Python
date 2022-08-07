from Controlador.Clientes import Cliente

class ArregloClientes:
    
    def __init__(self):
         self.dataClientes = []
      
    def adicionaCliente(self, objCli):
         self.dataClientes.append(objCli)

    def devolverCliente(self, pos):
        return self.dataClientes[pos]

    def tamañoArregloCliente(self):
        return len(self.dataClientes)

    def buscarCliente(self, dni):
        for i in range(self.tamañoArregloCliente()):
         if dni == self.dataClientes[i].getDNI():
           return i
        return -1

    def eliminarCliente(self, indice):
        del(self.dataClientes[indice])
