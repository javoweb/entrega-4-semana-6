import logging
import traceback
import pulsar, _pulsar
import aiopulsar
import asyncio
from pulsar.schema import Record, AvroSchema
from ...seedwork.infraestructura import utils
from ...seedwork.aplicacion.comandos import ejecutar_commando


async def suscribirse_a_topico(topico: str, suscripcion: str, schema: type[Record],
                               tipo_consumidor: _pulsar.ConsumerType = _pulsar.ConsumerType.Shared):
    try:
        async with aiopulsar.connect(f'pulsar://{utils.broker_host()}:6650') as cliente:
            async with cliente.subscribe(
                    topico,
                    consumer_type=tipo_consumidor,
                    subscription_name=suscripcion,
                    schema=AvroSchema(schema)
            ) as consumidor:
                while True:
                    mensaje = await consumidor.receive()
                    print(mensaje)
                    datos = mensaje.value()
                    print(f'Evento recibido: {datos}')
                    try:
                        ejecutar_commando(datos)
                    except Exception as e:
                        print(e)
                    await consumidor.acknowledge(mensaje)

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
