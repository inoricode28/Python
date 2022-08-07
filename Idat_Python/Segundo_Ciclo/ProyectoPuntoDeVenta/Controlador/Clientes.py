class Cliente:

   def __init__(self, dniCliente, nombreCliente, apellidoPaternoCliente, apellidoMaternoCliente, direccionCliente, telefonoCliente):
       self.__dniCliente = dniCliente
       self.__nombreCliente = nombreCliente
       self.__apellidoPaternoCliente = apellidoPaternoCliente
       self.__apellidoMaternoCliente = apellidoMaternoCliente
       self.__direccionCliente = direccionCliente
       self.__telefonoCliente = telefonoCliente

# Falta implementar los getters and setters

   def getDNI(self):
       return self.__dniCliente

   def getNombre(self):
      return self.__nombreCliente

   def getApellidoPaterno(self):
       return self.__apellidoPaternoCliente

   def getApellidoMaterno(self):
       return self.__apellidoMaternoCliente
     
   def getDireccion(self):
       return self.__direccionCliente

   def gettelefono(self):
       return self.__telefonoCliente

   def setDNI(self, dniCliente):
        self.__dniCliente = dniCliente

   def setNombre(self, nombreCliente):
        self.__nombreCliente = nombreCliente

   def setApellidoPaterno(self, apellidoPaternoCliente):
        self.__apellidoPaternoCliente = apellidoPaternoCliente

   def setApellidoMaterno(self, apellidoMaternoCliente):
        self.__apellidoMaternoCliente = apellidoMaternoCliente

   def setDireccion(self, direccionCliente):
        self.__direccionCliente = direccionCliente

   def settelefono(self, telefonoCliente):
        self.__telefonoCliente = telefonoCliente







