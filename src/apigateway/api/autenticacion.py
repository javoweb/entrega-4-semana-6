import apigateway.seedwork.presentacion.api as api
import json
from apigateway.modulos.autenticacion.aplicacion.servicios import ServicioAutentica
from flask import redirect, render_template, request, session, url_for
from flask import Response
from flask_jwt_extended import create_access_token
from apigateway.modulos.autenticacion.aplicacion.mapeadores import MapeadorUsuarioDTOJson

bp = api.crear_blueprint('login', '/apigateway')

@bp.route('/login', methods=('POST',))
def autenticar_usuario():
    print("realiza login with", request.json.get("username",None))
    user = request.json.get("username",None)
    password = request.json.get("password",None)
    print(user) 

    user_dict = request.json

    map_usuario = MapeadorUsuarioDTOJson()
    usuario_dto = map_usuario.externo_a_dto(user_dict)
    print(usuario_dto)

    if  not usuario_dto.user or not usuario_dto.password:
        return Response(json.dumps(dict(error=str('usuario o password deben ser diligenciados'))), status=401, mimetype='application/json')
    else:
        servicio = ServicioAutentica()        
        if not servicio.obtener_usuario_por_id(usuario_dto):
            return Response(json.dumps(dict(error=str('usuario o password son erroneos'))), status=401, mimetype='application/json')
        
        token = create_access_token(identity=user)
        return [{'token': token, 'username':user}]

    