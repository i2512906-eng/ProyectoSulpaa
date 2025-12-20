from capaDatos.dPersona import Dpersona

class NPersona:
    def __init__(self):
        self.__dPersona = Dpersona()

    def mostrarPersonas(self):
        return self.__dPersona.mostrarPersonas()

    def nuevaPersona(self, usuario:dict):
        self.__dPersona.nuevaPersona(usuario)
    
    def actualizarPersona(self, usuario:dict, nombre:str):
        return self.__dPersona.actualizarPersona(usuario, nombre)
    
    def eliminarPersona(self):
        pass
        
