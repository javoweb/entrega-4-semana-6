from pulsar.schema import String, Long, Record
from dataclasses import dataclass, field
from ....seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from ....seedwork.infraestructura.utils import time_millis
from . import TipoCliente
import uuid


class RegistrarUsuario(Record):
    nombres = String()
    apellidos = String()
    email = String()
    tipo_cliente = TipoCliente
    fecha_creacion = Long()


class ValidarUsuario(Record):
    id = String()
    fecha_validacion = Long()


class DesactivarUsuario(Record):
    id = String()
    fecha_desactivacion = Long()


class ComandoRegistrarUsuario(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="RegistrarUsuario")
    datacontenttype = String()
    service_name = String(default="edla.ordenes")
    data = RegistrarUsuario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ComandoValidarUsuario(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ValidarUsuario")
    datacontenttype = String()
    service_name = String(default="edla.ordenes")
    data = ValidarUsuario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ComandoDesactivarUsuario(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="DesactivarUsuario")
    datacontenttype = String()
    service_name = String(default="edla.ordenes")
    data = DesactivarUsuario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
