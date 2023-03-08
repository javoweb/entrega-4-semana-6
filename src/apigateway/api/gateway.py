import apigateway.seedwork.presentacion.api as api
import json
from flask import redirect, render_template, request, session, url_for
from flask import Response
from flask_jwt_extended import jwt_required

bp = api.crear_blueprint('adquisiciones', '/apigateway')

@bp.route('/adquisiciones', methods=('GET',))
@jwt_required()
def reservar_usando_comando():
    try:
        # NOTE Asignamos el valor 'pulsar' para usar la Unidad de trabajo de Pulsar y 
        # no la defecto de SQLAlchemy
        session['uow_metodo'] = 'pulsar'

        reserva_dict = request.json
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
