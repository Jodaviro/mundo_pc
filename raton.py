from dispositivoentrada import Dispositivoentrada

class Raton (Dispositivoentrada):
    
    contador_ratones = 0
    
    def __init__(self,marca, tipoEntrada):
        Raton.contador_ratones += 1
        self.contador_ratones = Raton.contador_ratones
        self.__id_raton = self.contador_ratones
        super().__init__(marca, tipoEntrada)
        # self._tipoEntrada= tipoEntrada
        # self._marca= marca 
        
    def __str__(self):
        return (
        f"id : {self.__id_raton} "
        f"Tipo de entrada: {self._tipoEntrada}  "
        f"Marca: {self._marca} \n "  
        )    
