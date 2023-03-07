from adquisiciones.seedwork.aplicacion.queries import QueryHandler
from adquisiciones.modulos.adquisiciones.infraestructura.fabricas import FabricaRepositorio
from adquisiciones.modulos.adquisiciones.dominio.fabricas import FabricaAdquisicion

class PedidoQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_adquisicion: FabricaAdquisicion = FabricaAdquisicion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_adquisicion(self):
        return self._fabrica_adquisicion 