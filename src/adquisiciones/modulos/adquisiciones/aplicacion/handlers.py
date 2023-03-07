from adquisiciones.modulos.adquisiciones.dominio.eventos import AdquisicionCreada
from adquisiciones.seedwork.aplicacion.handlers import Handler
from adquisiciones.modulos.adquisiciones.infraestructura.despachadores import Despachador

class HandlerAdquisicionIntegracion(Handler):

    @staticmethod
    def handle_adquisicion_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-adquisiciones') 