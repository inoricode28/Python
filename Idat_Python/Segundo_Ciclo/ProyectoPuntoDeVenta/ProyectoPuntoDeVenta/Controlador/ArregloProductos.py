from Controlador.Productos import Producto

class ArregloProductos:

    def __init__(self):
        self.dataProductos = []
    
    def adicionaProducto(self, objPro):
        self.dataProductos.append(objPro)
    
    def devolverProducto(self, pos):
        return self.dataProductos[pos]
    
    def tamañoArregloProducto(self):
        return len(self.dataProductos)
    
    def buscarProducto(self, codigo):
        for i in range(self.tamañoArregloProducto()):
            if codigo == self.dataProductos[i].getCodigo():
                return i
        return -1
    
    def eliminarProducto(self, indice):
        del(self.dataProductos[indice])