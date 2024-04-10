from pydantic import BaseModel, Field
from typing import Optional

class CategoriaEgresos (BaseModel):
    id: Optional[int] = Field(default=None, gt= 0, title="Id de la categoria")
    nombre: str = Field(title="Nombre de la categoria")
    descripcion: Optional[str] = Field(default=None, title="Descripcion de la categoria")

    class Config:
            json_schema_extra = {
                "example": {
                    "id": 1,
                    "nombre": "Arriendo",
                    "descripcion": "Pago de arriendo"
                }
            }