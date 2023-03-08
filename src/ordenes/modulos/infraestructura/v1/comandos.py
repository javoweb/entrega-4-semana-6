from pulsar.schema import String, Long, Record, Array
from ....seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from ....seedwork.infraestructura.utils import time_millis
import uuid


class CrearOrden(Record):
    nombres = String()
    apellidos = String()
    email = String()
    direccion = String()
    productos = Array(String())
    fecha_creacion = Long()


class ComandoCrearOrden(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="CrearOrden")
    datacontenttype = String()
    service_name = String(default="edla.ordenes")
    data = CrearOrden

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
