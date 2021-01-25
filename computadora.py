from teclado import Teclado
from raton import Raton
from monitor import Monitor

class Computadora:
    """ Clase Computadora recibe STR nombre"""
    
    contadorComputadoras= 0
    
    def __init__(self, nombre): 
        Computadora.contadorComputadoras +=1
        self.contadorComputadora = Computadora.contadorComputadoras 
        self.__idComputadora = self.contadorComputadoras
        self.__nombre= nombre
        self.__monitor=False
        self.__teclado=False
        self.__raton= False
        
    
    def get_idComputadora (self):
        return self.__idComputadora
    
    def set_idComputadora (self, idComputadora):
        self.__idComputadora = idComputadora
       
    def get_nombre (self):
        return self.__nombre
    
    def set_nombre (self, nombre):
        self.__nombre = nombre
        

    def get_monitor (self):
        return self.__monitor
    
    def set_monitor (self, monitor):
        self.__monitor = monitor
    
    def get_teclado (self):
        return self.__teclado
    
    def set_teclado (self, teclado):
        self.__teclado = teclado
        
    def get_nombre (self):
        return self.__raton
    
    def set_raton (self, raton):
        self.__raton = raton
    
    def __str__ (self):
        return (f"""
        {self.__nombre}: {self.__idComputadora}
        Monitor: {self.__monitor} 
        Teclado: {self.__teclado} 
        Raton: {self.__raton}
        """
        )
