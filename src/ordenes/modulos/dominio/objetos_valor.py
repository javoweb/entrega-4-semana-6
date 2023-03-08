"""Objetos valor del dominio de ordenes

En este archivo usted encontrará los objetos valor del dominio de ordenes

"""

from ...seedwork.dominio.objetos_valor import ObjetoValor, Ciudad
from dataclasses import dataclass


@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombres: str
    apellidos: str


@dataclass(frozen=True)
class Email(ObjetoValor):
    address: str

@dataclass(frozen=True)
class Direccion(ObjetoValor):
    calle_principal: str
    calle_secundaria: str
    numero: str
    referencia: str


@dataclass(frozen=True)
class Producto(ObjetoValor):
    nombre: str
    cantidad: int
