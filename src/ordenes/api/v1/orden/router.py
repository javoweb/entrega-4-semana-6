from fastapi import APIRouter, status, BackgroundTasks
from ....modulos.aplicacion.comandos.crear_orden import \
    ComandoCrearOrden
from ....seedwork.presentacion.dto import RespuestaAsincrona
from ....seedwork.aplicacion.comandos import ejecutar_commando
from ....seedwork.aplicacion.queries import ejecutar_query

from .dto import RegistrarUsuario

router = APIRouter()


@router.post("/crear", status_code=status.HTTP_202_ACCEPTED,
             response_model=RespuestaAsincrona)
async def crear_orden(registrar_usuario: RegistrarUsuario,
                      background_tasks: BackgroundTasks) -> RespuestaAsincrona:
    comando = ComandoCrearOrden(
        nombres=registrar_usuario.nombres,
        apellidos=registrar_usuario.apellidos,
        email=registrar_usuario.email,
        password=registrar_usuario.password,
        es_empresarial=registrar_usuario.es_empresarial
    )
    background_tasks.add_task(ejecutar_commando, comando)
    return RespuestaAsincrona(mensaje="Registro de orden en proceso")
