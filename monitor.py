class Monitor:
    """Clase monitor, recibe marca STR y tamano INT   """
    contadorMonitores= 0
    
    def __init__(self, marca, tamano):
        Monitor.contadorMonitores +=1
        self.contadorMonitores= Monitor.contadorMonitores
        self.__idmonitor = self.contadorMonitores
        self.__marca = marca
        self.__tamano= tamano


    def get_idmonitor (self):
        return self.__idmonitor
    
    def set_idmonitor (self, idmonitor):
        self.__idmonitor = idmonitor 
     
    def get_marca (self):
        return self.__marca 
        
    def set_marca (self, marca):
        self.__marca = marca
        
    def set_tamano (self, tamano):
        self.__tamano = tamano
    
    def get_tamano (self):
        return self.__tamano
        
    def __str__ (self):
        return(
         f"Id: {self.__idmonitor} "
         f"Marca: {self.__marca} "
         f"Tamano:{self.__tamano} "   
        )
