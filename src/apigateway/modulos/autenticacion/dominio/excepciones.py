""" Excepciones del dominio de ApiGateWay

En este archivo usted encontrará los Excepciones relacionadas
al dominio del ApiGateWay

"""

from apigateway.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioApiGateWayExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de ApiGateWay'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)