from dataclasses import dataclass
from adquisiciones.seedwork.aplicacion.queries import Query, QueryResultado
from adquisiciones.seedwork.aplicacion.queries import ejecutar_query as query
from adquisiciones.modulos.adquisiciones.infraestructura.repositorios import RepositorioAdquisicion
from adquisiciones.modulos.adquisiciones.aplicacion.mapeadores import MapeadorAdquisicion
from .base import AdquisicionQueryBaseHandler

@dataclass
class ObtenerAdquisicion(Query):
    id: str

class ObtenerAdquisicionHandler(AdquisicionQueryBaseHandler):
    def handle(self, query: ObtenerAdquisicion) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAdquisicion.__class__)
        adquisicion = self.fabrica_adquisicion.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorAdquisicion())
        return QueryResultado(resultado = adquisicion)

@query.register(ObtenerAdquisicion)
def ejecutar_query_obtener_adquisicion(query: ObtenerAdquisicion):
    handler = ObtenerAdquisicionHandler()
    return handler.handle(query)