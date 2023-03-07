from pulsar.schema import *
from adquisiciones.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class AdquisicionCreadaPayload(Record):
    producto = String()
    cantindad = Integer()
    fecha = String()

class EventoAdquisicionCreada(EventoIntegracion):
    data = AdquisicionCreadaPayload() 