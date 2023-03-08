"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations
from dataclasses import dataclass, field

import apigateway.modulos.autenticacion.dominio.objetos_valor as ov
from apigateway.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad


@dataclass
class Aeropuerto(Locacion):
    codigo: ov.Codigo = field(default_factory=ov.Codigo)
    nombre: ov.NombreAero = field(default_factory=ov.NombreAero)

    def __str__(self) -> str:
        return self.codigo.codigo.upper()

@dataclass
class Usuario():
    user: ov.User = field(default_factory=ov.User)
    password: ov.PassWord = field(default_factory=ov.PassWord)


@dataclass
class Pasajero(Entidad):
    clase: ov.Clase = field(default_factory=ov.Clase)
    tipo: ov.TipoUsuario = field(default_factory=ov.TipoUsuario)


@dataclass
class Reserva(AgregacionRaiz):
    itinerarios: list[ov.Itinerario] = field(default_factory=list[ov.Itinerario])

@dataclass
class Proveedor(Entidad):
    codigo: ov.Codigo = field(default_factory=ov.Codigo)
    nombre: ov.NombreAero = field(default_factory=ov.NombreAero)
    itinerarios: list[ov.Itinerario] = field(default_factory=list[ov.Itinerario])

    def obtener_itinerarios(self, odos: list[Odo], parametros: ParametroBusca):
        return self.itinerarios
