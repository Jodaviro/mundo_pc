from dispositivoentrada import Dispositivoentrada

class Teclado (Dispositivoentrada):
    
    contador_teclados = 0
    
    def __init__(self,marca, tipoEntrada):
        Teclado.contador_teclados += 1
        self.contador_teclados = Teclado.contador_teclados
        self.__id_teclados = self.contador_teclados
        super().__init__(marca, tipoEntrada)
        # self._tipoEntrada= tipoEntrada
        # self._marca= marca 
        
    def __str__(self):
        return (
        f"id: {self.__id_teclados}  "    
        f"Tipo de entrada: {self._tipoEntrada} "
        f"Marca: {self._marca} n"  
        )  