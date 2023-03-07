from adquisiciones.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioAdquisicionesExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de Adquisicion'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)