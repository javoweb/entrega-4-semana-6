from dataclasses import dataclass
from adquisiciones.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class AdquisicionDTO(DTO):
    producto: str 
    cantidad: int
    fecha: str