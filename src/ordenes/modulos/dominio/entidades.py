"""Entidades del dominio de ordenes

En este archivo usted encontrará las entidades del dominio de ordenes

"""

from datetime import datetime
from typing import List

from ...seedwork.dominio.entidades import AgregacionRaiz
from dataclasses import dataclass, field

from .objetos_valor import Nombre, Email, Producto

@dataclass
class Orden(AgregacionRaiz):
    nombre_cliente: Nombre = field(default_factory=Nombre)
    email: Email = field(default_factory=Email)
    direccion: str = field(default_factory=str)
    productos: List[Producto] = field(default_factory=List[Producto])
