from dataclasses import dataclass, field
from apigateway.seedwork.aplicacion.comandos import Comando

@dataclass
class LlamarMsEmpaquetado(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    #id: str
    #itinerarios: list[ItinerarioDTO]

class LlamarAplicacionHandler():
    