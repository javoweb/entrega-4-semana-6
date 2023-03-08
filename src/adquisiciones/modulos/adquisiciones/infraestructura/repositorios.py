from adquisiciones.config.db import db
from adquisiciones.modulos.adquisiciones.dominio.repositorios import RepositorioAdquisicion
from adquisiciones.modulos.adquisiciones.dominio.entidades import Adquisicion
from adquisiciones.modulos.adquisiciones.dominio.fabricas import FabricaAdquisicion
from .dto import Adquisicion as AdquisicionDTO
from .mapeadores import MapeadorAdquisicion
from uuid import UUID

class RepositorioAdquisicionSQLite(RepositorioAdquisicion):

    def __init__(self):
        self._fabrica_adquisicion: FabricaAdquisicion = FabricaAdquisicion()

    @property
    def fabrica_adquisicion(self):
        return self._fabrica_adquisicion

    def obtener_por_id(self, id: UUID) -> Adquisicion:
        adquisicion_dto = db.session.query(AdquisicionDTO).filter_by(id=str(id)).one()
        return adquisicion_dto
    
    def obtener_todos(self) -> list[Adquisicion]:
        # TODO
        raise NotImplementedError
    
    def agregar(self, entity: Adquisicion):
        adquisicion_dto = self.fabrica_adquisicion.crear_objeto(entity, MapeadorAdquisicion())
        db.session.add(adquisicion_dto)
        # db.session.commit()
    
    def actualizar(self, entity: Adquisicion):
        # TODO
        raise NotImplementedError
    
    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError