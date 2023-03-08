from typing import List

from pydantic import BaseModel


class CrearOrden(BaseModel):
    nombres: str
    apellidos: str
    email: str
    productos: List[str]
