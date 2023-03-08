from adquisiciones.seedwork.aplicacion.comandos import ComandoHandler
from adquisiciones.modulos.adquisiciones.infraestructura.fabricas import FabricaRepositorio
from adquisiciones.modulos.adquisiciones.dominio.fabricas import FabricaAdquisicion

class CrearAdquisicionBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_adquisicion: FabricaAdquisicion = FabricaAdquisicion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_adquisicion(self):
        return self._fabrica_adquisicion