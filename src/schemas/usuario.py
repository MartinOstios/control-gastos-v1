from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Usuario (BaseModel):
    id: Optional[int] = Field(default=None , gt=0, title="El id del usuario")
    email: str = Field(title="El email del usuario")
    nombre: str = Field(title="El nombre del usuario")
    contraseña: str = Field(title="La contraseña del usuario")
    activo: bool = Field(default=True, title="Si está activo o no el usuario")
    
    class Config:
        from_attributes = True
        json_schema_extra = {
        "example": {
        "email": "pepe@base.net",
        "nombre": "Pepe Pimentón",
        "contraseña": "xxx",
        "activo": 1
        }
    }
        
class UsuarioCreado (BaseModel):
    nombre: str = Field(min_length=4, max_length=60, title="Name of the user")
    email: EmailStr = Field(min_length=6, max_length=64, title="Email of theuser")
    contraseña: str = Field(max_length=64, title="Password of the user")
    activo: bool = Field(default=True, title="If the user is active or not")
    
class UsuarioLogin (BaseModel):
    email: EmailStr = Field(min_length=6, max_length=64, alias="username",title="Email of the user")
    contraseña: str = Field(min_length=4, title="Password of the user")