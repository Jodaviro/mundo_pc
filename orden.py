
class Orden ():
    """ Clase Orden recibe LIST de computadora """
    contadorOrdenes=0
    
    def __init__(self,computadora):
        Orden.contadorOrdenes += 1
        self.contadorOrdenes = Orden.contadorOrdenes
        self.__idOrden= self.contadorOrdenes
        self.__computadoras = computadora
        
        
    def agregarComputadora(self,computadora):
        self.__computadoras.append(computadora)

    def set_computadora(self,computadora):
        self.__computadoras= computadora
        
    def get_computadora(self):
        return self.__computadora
    
    def get_idOrden(self):
        return self.__idOrden
    
    
    def set_idOrden(self,numerorden):
        self.__idOrden= numerorden
        

    def __str__(self):
        computadoras_str=" "
        for computadora in self.__computadoras :
            computadoras_str += computadora.__str__()
        return(
        f"Orden: {self.__idOrden}, Computadoras: \n"
        f"\n{computadoras_str}"     
        )