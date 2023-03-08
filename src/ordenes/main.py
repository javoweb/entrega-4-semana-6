from fastapi import FastAPI
from .config.api import app_configs, settings
from .api.v1.router import router as v1

from .modulos.infraestructura.consumidores import suscribirse_a_topico
from .modulos.infraestructura.v1.eventos import EventoOrdenes, OrdenCreada
from .modulos.infraestructura.v1.comandos import ComandoCrearOrden, CrearOrden
from .modulos.infraestructura.despachadores import Despachador
from .seedwork.infraestructura import utils

import asyncio
import time
import traceback
import uvicorn

app = FastAPI(**app_configs)
tasks = list()


@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(
        suscribirse_a_topico("evento-usuarios", "sub-cliente", EventoOrdenes))
    task2 = asyncio.ensure_future(
        suscribirse_a_topico("comando-crear-orden", "sub-com-crear-orden",
                             ComandoCrearOrden))
    tasks.append(task1)
    tasks.append(task2)


@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()


@app.get("/prueba-crear-orden", include_in_schema=False)
async def prueba_crear_orden() -> dict[str, str]:
    payload = CrearOrden(
        nombres="Juan",
        apellidos="Urrego",
        email="js.urrego110@aeroalpes.net",
        tipo_cliente=1,
        fecha_creacion=utils.time_millis()
    )

    comando = ComandoCrearOrden(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=CrearOrden.__name__,
        data=payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-crear-orden")
    return {"status": "ok"}

@app.get("/health", include_in_schema=False)
async def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(v1, prefix="/v1", tags=["Version 1"])
