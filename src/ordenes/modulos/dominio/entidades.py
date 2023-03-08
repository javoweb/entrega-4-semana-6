"""Entidades del dominio de ordenes

En este archivo usted encontrará las entidades del dominio de ordenes

"""

from datetime import datetime
from typing import List

from ...seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field

from .objetos_valor import Nombre, Email, Direccion, Producto

@dataclass
class Orden(AgregacionRaiz):
    nombre_cliente: Nombre = field(default_factory=Nombre)
    email: Email = field(default_factory=Email)
    direccion: Direccion = field(default_factory=Direccion)
    productos: List[Producto] = field(default_factory=List[Producto])
