import adquisiciones.seedwork.presentacion.api as api
import json
from adquisiciones.seedwork.dominio.excepciones import ExcepcionDominio
from adquisiciones.seedwork.aplicacion.queries import ejecutar_query
from adquisiciones.seedwork.aplicacion.comandos import ejecutar_commando
from flask import Response, request
from adquisiciones.modulos.adquisiciones.aplicacion.mapeadores import MapeadoradquisicionesDTOJson
from adquisiciones.modulos.adquisiciones.aplicacion.comandos.crear_adquisiciones import Crearadquisiciones
from adquisiciones.modulos.adquisiciones.aplicacion.queries.obtener_adquisiciones import Obteneradquisiciones

bp = api.crear_blueprint('adquisiciones', '/adquisiciones')

@bp.route('/adquisiciones-comando', methods=('POST',))
def reservar_asincrona():

    try:
        adquisiciones_dict = request.json

        map_adquisiciones = MapeadoradquisicionesDTOJson()
        adquisiciones_dto = map_adquisiciones.externo_a_dto(adquisiciones_dict) 

        comando = Crearadquisiciones(id_client=adquisiciones_dto.id_client, 
            fecha_orden=adquisiciones_dto.fecha_orden, 
            numero_orden=adquisiciones_dto.numero_orden)
        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/<id>', methods=('GET',))
def get_adquisiciones(id=None):
    if id:
        query_resultado = ejecutar_query(Obteneradquisiciones(id))
        map_adquisiciones = MapeadoradquisicionesDTOJson()
        return map_adquisiciones.dto_a_externo(query_resultado.resultado)
    else: 
        return [{'message': 'GET!'}]
