from pulsar.schema import String, Long, Record
from ....seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from ....seedwork.infraestructura.utils import time_millis
from . import TipoCliente
import uuid


class UsuarioRegistrado(Record):
    id = String()
    nombres = String()
    apellidos = String()
    email = String()
    tipo_cliente = TipoCliente
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
    usuario_registrado = UsuarioRegistrado
    usuario_validado = UsuarioValidado
    usuario_desactivado = UsuarioDesactivado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
