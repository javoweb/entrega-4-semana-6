from __future__ import annotations
from dataclasses import dataclass, field
from adquisiciones.seedwork.dominio.entidades import AgregacionRaiz
from adquisiciones.modulos.adquisiciones.dominio.eventos import AdquisicionCreada
from datetime import datetime
import uuid

@dataclass
class adquisicion(AgregacionRaiz):
    producto: str = field(default=None)
    fecha: datetime = field(default=None)
    cantidad: int = field(default=None)

    def crear_adquisicion(self, adquisicion: Adquisicion):
        #self.estado = adquisicion.estado
        self.agregar_evento(AdquisicionCreada(producto=self.producto, cantidad=self.cantidad, fecha=self.fecha))