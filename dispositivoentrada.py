class Dispositivoentrada :
    
    def __init__ (self, marca, tipoEntrada):
        self._tipoEntrada= tipoEntrada
        self._marca= marca   
        
        
    def get_tipoEntrada (self):
        return self._tipoEntrada
    
    def set_tipoEntrada (self,tipoEntrada):
        self._tipoEntrada=tipoEntrada
        
    def get_marca (self):
        return self._marca
    
    def set_marca (self, marca):
        self._marca = marca

    # def __str__ (self):
    #     return self._tipoEntrada +', ' + self._marca        