from __future__ import annotations
from dataclasses import dataclass
from adquisiciones.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class AdquisicionCreada(EventoDominio):
    producto: str = None
    cantidad: int = None
    fecha: datetime = None