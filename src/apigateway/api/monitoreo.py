import apigateway.seedwork.presentacion.api as api
import requests
import os
import datetime
import json
from flask_jwt_extended import jwt_required

bp = api.crear_blueprint('monitoreo', '/apigateway')
@bp.route('/monitoreo', methods=('GET',))

def ping_echo():
    return [{'servicio': 'disponible'}]

@bp.route('/monitoreo/adquisiciones', methods=('GET',))
def ping():
    """Función que determina si el recurso remoto esta activo.
    Args:
        url (str): URL a consultar
    Returns:
        bool: Estado del recurso consultado
    """
    r = requests.get("http://localhost:5000/apigateway/adquisiciones/echo")
    return r.status_code == requests.codes.ok


def get(self):
        """Get Method of MonitorView."""

        # obtiene las variables de entorno
        url_recurso = "http://localhost:5000/apigateway/adquisiciones/echo"
        """
        url_notification = os.getenv("URL_NOTIFICACION")
        time_up = float(os.getenv("TIME_UP", default="0.0"))
        time_down = float(os.getenv("TIME_DOWN", default="0.0"))
        events = int(os.getenv("EVENTS", default="0"))
        date_ini = os.getenv("DATE_INI", default="")
        date_flag = datetime.datetime.strptime(
            os.getenv("DATE_FLAG", default="2023-03-07 12:00:00"),
            "%Y-%m-%d %H:%M:%S")
        prev = int(os.getenv("PREV", default="1"))

        # almacena la fecha inicial del proceso de monitoreo
        if len(date_ini) == 0:
            date_flag = datetime.datetime.now()
            date_ini = date_flag.strftime("%Y-%m-%d %H:%M:%S")
"""
        # dependiendo del estado del recurso remoto
        # define el tipo de comunicación
        if self.ping(url_recurso):
            # define la comunicación a sincrónica
            new_mode = "sync"
            message = "recurso ok"
            status = 200

            # viene de un estado de comunicacion asincrónica
            if prev == 0:
                # aumenta el contador de tiempo indisponible
                td = datetime.datetime.now() - date_flag
                time_down += td.seconds
                # guarda la fecha del cambio de estado
                date_flag = datetime.datetime.now()
                # define como estado previo el de indisponibilidad
                prev = 1
                # crea el mensaje de notificacion
                msg = "Restablecimiento del microservicio APPOINTMENTS\n"
                msg += "Fecha restablecimiento: {}\n".format(date_flag)
                msg += "Tiempo activo acumulado: {}\n".format(time_up)
                msg += "Tiempo inactivo acumulado: {}\n".format(time_down)
                msg += "Eventos acumulados: {}\n".format(events)

                # envía mensaje de notificación
                res = self.send_notification("slack.webhook", msg)

        else:
            # define la comunicación a asincrónica
            new_mode = "async"
            message = "el recurso no ha respondido satisfactoriamente"
            status = 500

            # viene de un estado de comunicacion sincrónica
            if prev == 1:
                # aumenta el contador de tiempo disponible
                td = datetime.datetime.now() - date_flag
                time_up += td.seconds
                # cambia la fecha de estado
                date_flag = datetime.datetime.now()
                # defiene como estado previo el de dispopnible
                prev = 0
                # aumenta el contador de indisponibilidades
                events += 1
                # crea el mensaje de notificacion
                msg = "FALLA: Caida del microservicio Adquisiciones\n"
                msg += "Fecha caida: {}\n".format(date_flag)

                # envía mensaje de notificación
                res = self.send_notification("slack.webhook", msg)

        print(json.dumps({
            "type": "monitor status",
            "message": message,
            "url recurso": url_recurso
        }))

        return message, status

def send_notification(self, url: str, msg: str):
        """Función que activa la funcion de notificación.
        Args:
            url (str): URL del endpoint de notificación
            msg (str): Mensaje de notificación
        Returns:
            bool: Estado final de la solicitud de notificación
        """
        data = {
            "text": f"{msg}"
        }

        r = requests.post(
            url=url,
            json=data,
        )

        return r.status_code == requests.codes.ok