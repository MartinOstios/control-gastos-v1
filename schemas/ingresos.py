from pydantic import BaseModel, Field, validator
from typing import Optional
import datetime


class Ingreso (BaseModel):
    id: int = Field(gt=0, title="El id del registro del ingreso")
    fecha: datetime.date = Field(title="La fecha en la que se hizo el ingreso")
    descripcion: Optional[str] = Field(default=None, title="La descripción del ingreso")
    valor: float = Field(gt=0, title="El valor del ingreso")
    categoria: int = Field(gt=0, title="El ID de la categoría de ingreso")
    
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