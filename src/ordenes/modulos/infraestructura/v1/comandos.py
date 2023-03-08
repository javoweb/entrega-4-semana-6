from pulsar.schema import String, Long, Record
from dataclasses import dataclass, field
from ....seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from ....seedwork.infraestructura.utils import time_millis
from . import TipoCliente
import uuid


class CrearOrden(Record):
    nombres = String()
    apellidos = String()
    email = String()
    tipo_cliente = TipoCliente
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
