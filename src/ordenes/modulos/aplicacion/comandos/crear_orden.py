from abc import ABC, abstractmethod
from typing import List

from ...infraestructura.despachadores import Despachador
from ....modulos.dominio.entidades import Orden
from ....modulos.dominio.objetos_valor import Email, Nombre, Producto
from ....modulos.infraestructura.v1.comandos import ComandoCrearOrden, CrearOrden
from dataclasses import dataclass
import datetime
import time

from ....seedwork.infraestructura import utils


class Comando:
    ...


class ComandoHandler(ABC):
    @abstractmethod
    def handle(self, comando: Comando):
        raise NotImplementedError()


class CrearOrdenHandler(ComandoHandler):

    def a_entidad(self, comando: ComandoCrearOrden) -> Orden:
        params = dict(
            nombre_cliente=Nombre(comando.data.nombres, comando.data.apellidos),
            email=Email(comando.data.email),
            direccion=comando.data.direccion,
            productos=[Producto(nombre, 1) for nombre in comando.data.productos],
            fecha_creacion=datetime.datetime.now(),
            fecha_actualizacion=datetime.datetime.now()
        )

        return Orden(**params)

    def handle(self, comando: ComandoCrearOrden):
        orden = self.a_entidad(comando)
        comando = ComandoCrearOrden(
            time=utils.time_millis(),
            ingestion=utils.time_millis(),
            datacontenttype=CrearOrden.__name__,
            data=orden
        )
        despachador = Despachador()
        despachador.publicar_mensaje(comando, "evento-orden-creada")
