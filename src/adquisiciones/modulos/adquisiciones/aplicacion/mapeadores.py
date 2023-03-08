from adquisiciones.seedwork.aplicacion.dto import Mapeador as AppMap
from adquisiciones.seedwork.dominio.repositorios import Mapeador as RepMap
from adquisiciones.modulos.adquisiciones.dominio.entidades import Adquisicion
from .dto import AdquisicionDTO
from datetime import datetime

class MapeadorAdquisicionDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> AdquisicionDTO:
        adquisicion_dto = AdquisicionDTO(
            producto=externo.get('producto'),
            cantidad=externo.get('cantidad'),
            fecha=externo.get('fecha')
        )
        return adquisicion_dto

    def dto_a_externo(self, dto: AdquisicionDTO) -> dict:
        return dto.__dict__

class MapeadorAdquisicion(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Adquisicion.__class__

    def entidad_a_dto(self, entidad: Adquisicion) -> AdquisicionDTO:
        return AdquisicionDTO(
            producto = str(entidad.producto), 
            fecha = datetime.strftime(entidad.fecha, self._FORMATO_FECHA), 
            cantidad = entidad.cantidad)

    def dto_a_entidad(self, dto: AdquisicionDTO) -> Adquisicion:
        adquisicion = Adquisicion(producto=dto.producto, fecha=dto.fecha, cantidad=dto.cantidad)
        return adquisicion