import os, requests, logging

class Adquisiciones():
    HOSTNAME_ENV: str = 'adquisiciones'
    REST_API_HOST: str = f'http://{os.getenv(HOSTNAME_ENV, default="localhost")}:5001'
    REST_API_ENDPOINT: str = '/adquisiciones/adquisiciones-comando'

    def CrearAdquisicion(self):
        dict_obj = {"producto": "vasos",
                    "cantidad": 50,
                    "fecha": "10/02/2022"}

        r = requests.post(f'{self.REST_API_HOST}{self.REST_API_ENDPOINT}', json=dict_obj)
        if r.status_code == 200:
            return "OK"
        else:
            return "FAILED"


def run():
    cliente_adquisiciones = Adquisiciones()
    cliente_adquisiciones.CrearAdquisicion()

if __name__ == '__main__':
    logging.basicConfig()
    run()