from pulsar.schema import *
from adquisiciones.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class AdquisicionCreadaPayload(Record):
    id_cliente = String()
    numero_orden = String()
    fecha_orden = String()

class EventoAdquisicionCreada(EventoIntegracion):
    data = AdquisicionCreadaPayload() 