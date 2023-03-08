from fastapi import APIRouter, status, BackgroundTasks
from ....modulos.aplicacion.comandos.crear_orden import \
    ComandoCrearOrden
from ....seedwork.presentacion.dto import RespuestaAsincrona
from ....seedwork.aplicacion.comandos import ejecutar_commando
from ....seedwork.aplicacion.queries import ejecutar_query

from .dto import CrearOrden

router = APIRouter()


@router.post("/crear", status_code=status.HTTP_202_ACCEPTED,
             response_model=RespuestaAsincrona)
async def crear_orden(crear_orden: CrearOrden,
                      background_tasks: BackgroundTasks) -> RespuestaAsincrona:
    comando = ComandoCrearOrden(
        nombres=crear_orden.nombres,
        apellidos=crear_orden.apellidos,
        email=crear_orden.email,
        password=crear_orden.password,
        es_empresarial=crear_orden.es_empresarial
    )
    background_tasks.add_task(ejecutar_commando, comando)
    return RespuestaAsincrona(mensaje="Registro de orden en proceso")
