from typing import List

from ....seedwork.aplicacion.comandos import Comando, ComandoHandler
from ....seedwork.aplicacion.comandos import ejecutar_commando as comando
from ....modulos.dominio.entidades import Orden
from ....modulos.dominio.objetos_valor import Email, Nombre, Producto
from dataclasses import dataclass
import datetime
import time


@dataclass
class ComandoCrearOrden(Comando):
    nombres: str
    apellidos: str
    email: str
    productos: List[str]


class CrearOrdenHandler(ComandoHandler):

    def a_entidad(self, comando: ComandoCrearOrden) -> Orden:
        params = dict(
            nombre=Nombre(comando.nombres, comando.apellidos),
            email=Email(comando.email),
            productos=[Producto(nombre, 1) for nombre in comando.productos],
            fecha_creacion=datetime.datetime.now(),
            fecha_actualizacion=datetime.datetime.now()
        )

        return Orden(**params)

    def handle(self, comando: ComandoCrearOrden):
        orden = self.a_entidad(comando)


@comando.register(ComandoCrearOrden)
def ejecutar_comando_crear_orden(comando: ComandoCrearOrden):
    handler = CrearOrdenHandler()
    handler.handle(comando)
