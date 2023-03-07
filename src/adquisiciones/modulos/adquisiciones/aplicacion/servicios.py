from adquisiciones.seedwork.aplicacion.servicios import Servicio
from adquisiciones.modulos.adquisiciones.dominio.fabricas import FabricaAdquisicion
from adquisiciones.modulos.adquisiciones.infraestructura.fabricas import FabricaRepositorio
from adquisiciones.modulos.adquisiciones.infraestructura.repositorios import RepositorioAdquisicion
from .dto import AdquisicionDTO
from .mapeadores import MapeadorAdquisicion

class ServicioAdquisicion(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_adquisicion: FabricaAdquisicion = FabricaAdquisicion()
    
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    def fabrica_adquisicion(self):
        return self._fabrica_adquisicion

    def obtener_adquisicion_por_id(self, id) -> AdquisicionDTO:
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioAdquisicion.__class__)
        return self.fabrica_adquisicion.crear_objeto(repositorio.obtener_por_id(id), MapeadorAdquisicion())