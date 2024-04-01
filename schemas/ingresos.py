from pydantic import BaseModel, Field, validator, model_validator
from typing import Any, Optional, List
import datetime


class Ingreso (BaseModel):
    id: int = Field(gt=0, title="El id del registro del ingreso")
    fecha: datetime.date = Field(title="Expiration date of the product")
    descripcion: Optional[str] = Field(default=None, title="La descripción del ingreso")
    valor: float = Field(gt=0, title="El valor del ingreso")
    categoria: int = Field(gt=0, title="El ID de la categoría")
    
    @validator("fecha")
    @classmethod
    def validate_no_poison(cls, value):
        hoy = datetime.date.today()
        if value > hoy:
            raise ValueError("La fecha no puede ser del futuro")
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "fecha": "2024-04-01",
                "descripcion": "El pago del salario",
                "valor": 1000000,
                "categoria": 1
            }
        }