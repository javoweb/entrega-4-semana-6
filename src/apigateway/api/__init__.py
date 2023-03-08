import os

from flask import Flask
from flask_jwt_extended import JWTManager

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    import apigateway.modulos.autenticacion.infraestructura.dto

def create_app(configuracion= None):
    app = Flask(__name__)

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

     # Inicializa la DB
    from apigateway.config.db import init_db
    init_db(app)

    from apigateway.config.db import db

    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()

    app.config['JWT_SECRET_KEY'] = "ultra-secreto"
    jwt = JWTManager(app)

    from . import autenticacion
    from . import monitoreo
    from . import adquisiciones
    app.register_blueprint(autenticacion.bp)
    app.register_blueprint(monitoreo.bp)
    app.register_blueprint(adquisiciones.bp)

    return app