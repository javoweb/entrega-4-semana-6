from apigateway.seedwork.aplicacion.servicios import Servicio
from apigateway.modulos.autenticacion.infraestructura.fabricas import FabricaRepositorio
from apigateway.modulos.autenticacion.infraestructura.repositorios import RepositorioUsuarios
from .dto import UsuarioDTO

class ServicioAutentica(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    def obtener_usuario_por_id(self,usuario_dto: UsuarioDTO) -> bool:
        print("servicio--UsuarioDTO")
        print(usuario_dto)
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioUsuarios.__class__)
        repo_usuario = repositorio.obtener_por_id(usuario_dto.user)
        print("que trajo de DB")
        print(repo_usuario)
        if not repo_usuario:
            return False
        else:
            return True