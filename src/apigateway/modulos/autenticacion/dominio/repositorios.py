""" Interfaces para los repositorios del dominio de usuarios

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de usuarios

"""

from abc import ABC
from apigateway.seedwork.dominio.repositorios import Repositorio

class RepositorioUsuarios(Repositorio, ABC):
    ...
    
class RepositorioReservas(Repositorio, ABC):
    ...

class RepositorioProveedores(Repositorio, ABC):
    ...