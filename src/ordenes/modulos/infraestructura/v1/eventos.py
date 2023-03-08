from pulsar.schema import String, Long, Record, Array
from ....seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from ....seedwork.infraestructura.utils import time_millis
import uuid


class OrdenCreada:
    id = String()
    nombres = String()
    apellidos = String()
    email = String()
    productos = Array(String())
    fecha_creacion = Long()


class EventoOrdenes(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoOrdenes")
    datacontenttype = String()
    service_name = String(default="edla.ordenes")
    orden_creada = OrdenCreada

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
