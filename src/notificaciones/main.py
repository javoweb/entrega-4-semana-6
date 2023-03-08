import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import os

def time_millis():
    return int(time.time() * 1000)


class EventoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class AdquisicionCreadaPayload(Record):
    producto = String()
    cantidad = Integer()
    fecha = String()

class EventoAdquisicionCreada(EventoIntegracion):
    data = AdquisicionCreadaPayload() 




HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")

client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')
consumer = client.subscribe('eventos-adquisiciones', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='adquisiciones-sub-eventos', schema=AvroSchema(EventoAdquisicionCreada))

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg.value().data)
    print('=========================================')

    print('==== Envía correo a usuario ====')

    consumer.acknowledge(msg)

client.close()