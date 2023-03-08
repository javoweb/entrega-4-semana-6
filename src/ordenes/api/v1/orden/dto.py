from pydantic import BaseModel


class CrearOrden(BaseModel):
    nombres: str
    apellidos: str
    email: str
    password: str
    es_empresarial: bool
