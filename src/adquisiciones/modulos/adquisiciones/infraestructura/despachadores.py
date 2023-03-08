import pulsar
from pulsar.schema import *

from adquisiciones.modulos.adquisiciones.infraestructura.schema.v1.eventos import EventoAdquisicionCreada, AdquisicionCreadaPayload
# from adquisicion.modulos.adquisiciones.infraestructura.schema.v1.comandos import ComandoCrearOrden, ComandoCrearOrdenPayload
from adquisiciones.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoAdquisicionCreada))
        publicador.send(mensaje)
        print('topico: ${topico}')
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = AdquisicionCreadaPayload(
            producto=str(evento.producto),             
            cantidad=str(evento.cantidad), 
            fecha=str(evento.fecha)
        )
        evento_integracion = EventoAdquisicionCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoAdquisicionCreada))

  