"""Entidades del dominio de ordenes

En este archivo usted encontrará las entidades del dominio de ordenes

"""

from datetime import datetime
from ...seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field

from .objetos_valor import Nombre, Email, Cedula, Rut

@dataclass
class Usuario(Entidad):
    nombre: Nombre = field(default_factory=Nombre)
    email: Email = field(default_factory=Email)

@dataclass
class ClienteNatural(Usuario, AgregacionRaiz):
    cedula: Cedula = None
    fecha_nacimiento: datetime = None

@dataclass
class ClienteEmpresa(Usuario, AgregacionRaiz):
    rut: Rut = None
    fecha_constitucion: datetime = None
