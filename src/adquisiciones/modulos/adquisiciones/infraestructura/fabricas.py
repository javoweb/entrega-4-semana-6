from dataclasses import dataclass, field
from adquisiciones.seedwork.dominio.fabricas import Fabrica
from adquisiciones.seedwork.dominio.repositorios import Repositorio
from adquisiciones.modulos.adquisiciones.dominio.repositorios import RepositorioAdquisicion
from .repositorios import RepositorioAdquisicionSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioAdquisicion:
            return RepositorioAdquisicionSQLite()
        elif obj == RepositorioAdquisicion.__class__:
            return RepositorioAdquisicionSQLite()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')