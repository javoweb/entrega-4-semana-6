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


class UsuarioValidado(Record):
    id = String()
    fecha_validacion = Long()


class UsuarioDesactivado(Record):
    id = String()
    fecha_desactivacion = Long()


class EventoUsuario(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoUsuario")
    datacontenttype = String()
    service_name = String(default="edla.ordenes")
    usuario_registrado = OrdenCreada
    usuario_validado = UsuarioValidado
    usuario_desactivado = UsuarioDesactivado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
