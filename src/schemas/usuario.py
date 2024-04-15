from pydantic import BaseModel, Field
from typing import Optional


class Usuario (BaseModel):
    id: Optional[int] = Field(default=None , gt=0, title="El id del usuario")
    email: str = Field(title="El email del usuario")
    nombre: str = Field(title="El nombre del usuario")
    contraseña: str = Field(title="La contraseña del usuario")
    activo: bool = Field(default=False, title="Si está activo o no el usuario")