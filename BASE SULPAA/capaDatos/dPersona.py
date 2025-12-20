from conexion import ConexionDB

class Dpersona:
    def __init__(self):
        self.__db = ConexionDB().conexionSupabase()
        self.__nombreTabla = 'usuario'

    def __ejecutarConsultas(self, consulta, tipoConsulta = None):
        try:
            if tipoConsulta == 'SELECT':
                resultado = consulta.execute().data
                return resultado
            else: 
                resultado = consulta.execute()
                return resultado
        except Exception as e:
            raise e

    def mostrarPersonas(self):
        consulta = self.__db.table(self.__nombreTabla).select('*')
        return self.__ejecutarConsultas(consulta, 'SELECT')
    
    def nuevaPersona(self, usuario:dict):
        consulta = self.__db.table(self.__nombreTabla).insert(usuario)
        return self.__ejecutarConsultas(consulta)
    
    def actualizarPersona(self, usuario:dict, nombre:str):
        consulta = self.__db.table(self.__nombreTabla).update(usuario).eq('nombre', nombre)
        return self.__ejecutarConsultas(consulta)
    
    def eliminarPersona(self, nombre: str):
        consulta = self.__db.table(self.__nombreTabla).delete().eq('nombre',nombre)
        return self.__ejecutarConsultas(consulta)
