
import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from adquisiciones.modulos.adquisiciones.infraestructura.schema.v1.eventos import EventoAdquisicionCreada
from adquisiciones.modulos.adquisiciones.infraestructura.schema.v1.comandos import ComandoCrearAdquisicion
from adquisiciones.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-adquisiciones', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='adquisiciones-sub-eventos', schema=AvroSchema(EventoAdquisicionCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-adquisiciones', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='adquisiciones-sub-comandos', schema=AvroSchema(ComandoCrearAdquisicion))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

            