from pulsar.schema import *
from dataclasses import dataclass, field
from adquisiciones.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearAdquisicionPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearAdquisicion(ComandoIntegracion):
    data = ComandoCrearAdquisicionPayload() 