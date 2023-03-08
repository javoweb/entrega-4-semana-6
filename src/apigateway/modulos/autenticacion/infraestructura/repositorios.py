""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from apigateway.config.db import db
from apigateway.modulos.autenticacion.dominio.repositorios import RepositorioUsuarios, RepositorioProveedores, RepositorioReservas
from apigateway.modulos.autenticacion.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from apigateway.modulos.autenticacion.dominio.entidades import Proveedor, Aeropuerto, Reserva, Usuario
from apigateway.modulos.autenticacion.dominio.fabricas import FabricaUsuarios, FabricaVuelos
from .dto import Reserva as ReservaDTO
from .dto import Usuario as UsuarioDTO
from .mapeadores import MapeadorUsuarios
from uuid import UUID

class RepositorioProveedoresSQLite(RepositorioProveedores):

    def obtener_por_id(self, id: UUID) -> Reserva:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Reserva]:
        origen=Aeropuerto(codigo="CPT", nombre="Cape Town International")
        destino=Aeropuerto(codigo="JFK", nombre="JFK International Airport")
        legs=[Leg(origen=origen, destino=destino)]
        segmentos = [Segmento(legs)]
        odos=[Odo(segmentos=segmentos)]

        proveedor = Proveedor(codigo=CodigoIATA(codigo="AV"), nombre=NombreAero(nombre= "Avianca"))
        proveedor.itinerarios = [Itinerario(odos=odos, proveedor=proveedor)]
        return [proveedor]

    def agregar(self, entity: Reserva):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Reserva):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError

class RepositorioUsuariosSQLite(RepositorioUsuarios):
    def __init__(self):
        self._fabrica_usuarios: FabricaUsuarios = FabricaUsuarios()

    @property
    def fabrica_usuarios(self):
        return self._fabrica_usuarios
    
    def obtener_por_id(self, user: str) -> Usuario:
        print("repositorio-->")
        print(user)
        usuario_dto = db.session.query(UsuarioDTO).filter_by(user=str(user)).one()
        print("repositorio-->usuarioEncontrado")
        print(usuario_dto)
        return self.fabrica_usuarios.crear_objeto(usuario_dto, MapeadorUsuarios())
    
    def obtener_todos(self) -> list[Usuario]:
        # TODO
        raise NotImplementedError

    def agregar(self, usuario: Usuario):
        usuario_dto = self.fabrica_usuarios.crear_objeto(usuario, MapeadorUsuarios())
        db.session.add(usuario_dto)
        db.session.commit()

    def actualizar(self, usuario: Usuario):
        # TODO
        raise NotImplementedError

    def eliminar(self, usuario_id: UUID):
        # TODO
        raise NotImplementedError




class RepositorioReservasSQLite(RepositorioReservas):

    def __init__(self):
        self._fabrica_vuelos: FabricaVuelos = FabricaVuelos()

    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos

    def obtener_por_id(self, id: UUID) -> Reserva:
        reserva_dto = db.session.query(ReservaDTO).filter_by(id=str(id)).one()
        return self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())

    def obtener_todos(self) -> list[Reserva]:
        # TODO
        raise NotImplementedError

    def agregar(self, reserva: Reserva):
        reserva_dto = self.fabrica_vuelos.crear_objeto(reserva, MapeadorReserva())
        db.session.add(reserva_dto)
        db.session.commit()

    def actualizar(self, reserva: Reserva):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError