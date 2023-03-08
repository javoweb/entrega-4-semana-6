from adquisiciones.seedwork.dominio.repositorios import Mapeador
from adquisiciones.modulos.adquisiciones.dominio.entidades import Adquisicion
from .dto import Adquisicion as AdquisicionDTO

class MapeadorAdquisicion(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Adquisicion.__class__

    def entidad_a_dto(self, entidad: Adquisicion) -> AdquisicionDTO:
        adquisicion_dto = AdquisicionDTO()
        adquisicion_dto.id = str(entidad.id)
        adquisicion_dto.fecha_creacion = entidad.fecha_creacion
        adquisicion_dto.fecha_actualizacion = entidad.fecha_actualizacion
        adquisicion_dto.producto = entidad.producto
        adquisicion_dto.fecha = entidad.fecha
        adquisicion_dto.cantidad = entidad.cantidad

        return adquisicion_dto

    def dto_a_entidad(self, dto: AdquisicionDTO) -> Adquisicion:
        adquisicion = Adquisicion(producto=dto.producto, 
        fecha=dto.fecha, 
        cantidad=dto.cantidad)

        return adquisicion