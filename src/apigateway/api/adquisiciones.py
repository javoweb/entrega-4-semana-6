import apigateway.seedwork.presentacion.api as api
from flask_jwt_extended import jwt_required

bp = api.crear_blueprint('adquisiciones', '/apigateway')
@bp.route('/adquisiciones', methods=('POST',))
@jwt_required()
def consultar_adquisicion():
    return [{'servicio': 'disponible'}]


@bp.route('/adquisiciones/echo', methods=('GET',))
def ping_echo():
    return [{'servicio': 'disponible'}]