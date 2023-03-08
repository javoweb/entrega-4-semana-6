from dataclasses import dataclass
from adquisiciones.seedwork.dominio.repositorios import Mapeador
from adquisiciones.seedwork.dominio.fabricas import Fabrica
from adquisiciones.seedwork.dominio.entidades import Entidad
from .entidades import Adquisicion
from .excepciones import TipoObjetoNoExisteEnDominioAdquisicionesExcepcion

@dataclass
class _FabricaAdquisicion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            adquisicion: Adquisicion = mapeador.dto_a_entidad(obj)
            return adquisicion

@dataclass
class FabricaAdquisicion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Adquisicion.__class__:
            fabrica = _FabricaAdquisicion()
            return fabrica.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioAdquisicionesExcepcion()