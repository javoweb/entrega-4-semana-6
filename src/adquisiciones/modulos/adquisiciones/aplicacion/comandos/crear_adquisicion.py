from adquisiciones.seedwork.aplicacion.comandos import Comando
from adquisiciones.seedwork.aplicacion.comandos import ejecutar_commando as comando
from adquisiciones.modulos.adquisiciones.aplicacion.dto import AdquisicionDTO
from adquisiciones.modulos.adquisiciones.infraestructura.repositorios import RepositorioAdquisicion
from adquisiciones.modulos.adquisiciones.aplicacion.mapeadores import MapeadorAdquisicion
from adquisiciones.modulos.adquisiciones.dominio.entidades import Adquisicion

from dataclasses import dataclass
from .base import CrearadquisicionBaseHandler

from adquisicion.seedwork.infraestructura.uow import UnidadTrabajoPuerto

@dataclass
class CrearAdquisicion(Comando):
    producto: str
    fecha: str
    cantidad: int

class CrearAdquisicionHandler(CrearAdquisicionBaseHandler):
    def handle(self, comando: CrearAdquisicion):
        adquisicion_dto = AdquisicionDTO(
            producto=comando.producto, 
            fecha=comando.fecha, 
            cantidad=comando.cantidad)
        adquisicion: Adquisicion = self.fabrica_adquisicion.crear_objeto(adquisicion_dto, MapeadorAdquisicion())
        adquisicion.crear_adquisicion(adquisicion)
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAdquisicion.__class__)
        #repositorio.agregar(pedido)
        
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, adquisicion)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register(CrearAdquisicion)
def ejecutar_comando_crear_adquisicion(comando: CrearAdquisicion):
    handler = CrearAdquisicionHandler()
    handler.handle(comando)