import os, logging

from flask import Flask, jsonify
from flask_swagger import swagger

# Identifica el directorio baseapp.logger.info("Texto Id: ")
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import adquisiciones.modulos.adquisiciones.aplicacion

### Models Alchemy
def importar_modelos_alchemy():
    import adquisiciones.modulos.adquisiciones.infraestructura.dto

### Subscripcion a Pulsar
#def comenzar_consumidor(app):
 #   import threading
 #   import adquisiciones.modulos.adquisiciones.infraestructura.consumidores as adquisiciones

    ### Subscripcion eventos
#    threading.Thread(target=adquisiciones.suscribirse_a_eventos, args=[app]).start()

    #Subscripcion comandos
  #  threading.Thread(target=adquisiciones.suscribirse_a_comandos, args=[app]).start()

### App Flask
def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    logging.basicConfig(level=logging.DEBUG)
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

     # Inicializa la DB
    from adquisiciones.config.db import init_db
    init_db(app)

    from adquisiciones.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        #if not app.config.get('TESTING'):
            #comenzar_consumidor(app)

     # Importa Blueprints
    from . import adquisiciones

    # Registro de Blueprints
    app.register_blueprint(adquisiciones.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Adquisiciones API"
        return jsonify(swag)

    @app.route("/ping")
    def health():
        return {"echo": "microservicio adquisiciones up"}

    return app