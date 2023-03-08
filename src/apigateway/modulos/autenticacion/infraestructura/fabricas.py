""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from apigateway.seedwork.dominio.fabricas import Fabrica
from apigateway.seedwork.dominio.repositorios import Repositorio
from apigateway.modulos.autenticacion.dominio.repositorios import RepositorioUsuarios
from .repositorios import RepositorioUsuariosSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioUsuarios.__class__:
            return RepositorioUsuariosSQLite()
        else:
            raise ExcepcionFabrica()