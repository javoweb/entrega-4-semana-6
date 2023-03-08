import adquisiciones.seedwork.presentacion.api as api
import json
from adquisiciones.seedwork.dominio.excepciones import ExcepcionDominio
from adquisiciones.seedwork.aplicacion.queries import ejecutar_query
from adquisiciones.seedwork.aplicacion.comandos import ejecutar_commando
from flask import redirect, render_template, request, session, url_for
from flask import Response
from adquisiciones.modulos.adquisiciones.aplicacion.mapeadores import MapeadorAdquisicionDTOJson
from adquisiciones.modulos.adquisiciones.aplicacion.comandos.crear_adquisicion import CrearAdquisicion
from adquisiciones.modulos.adquisiciones.aplicacion.queries.obtener_adquisicion import ObtenerAdquisicion

bp = api.crear_blueprint('adquisiciones', '/adquisiciones')

@bp.route('/adquisiciones-comando', methods=('POST',))
def reservar_asincrona():

    try:
        adquisiciones_dict = request.json

        map_adquisiciones = MapeadorAdquisicionDTOJson()
        adquisiciones_dto = map_adquisiciones.externo_a_dto(adquisiciones_dict) 

        comando = CrearAdquisicion(producto=adquisiciones_dto.producto, 
            fecha=adquisiciones_dto.fecha, 
            cantidad=adquisiciones_dto.cantidad)
        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/<id>', methods=('GET',))
def get_adquisiciones(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerAdquisicion(id))
        map_adquisiciones = MapeadorAdquisicionDTOJson()
        return map_adquisiciones.dto_a_externo(query_resultado.resultado)
    else: 
        return [{'message': 'GET!'}]
