from functools import singledispatch

from ...modulos.aplicacion.comandos.crear_orden import CrearOrdenHandler
from ...modulos.infraestructura.v1.comandos import ComandoCrearOrden


@singledispatch
def ejecutar_commando(comando):
    raise NotImplementedError(f'No existe implementación para el comando de tipo {type(comando).__name__}')


@ejecutar_commando.register(ComandoCrearOrden)
def ejecutar_comando_crear_orden(comando: ComandoCrearOrden):
    handler = CrearOrdenHandler()
    handler.handle(comando)