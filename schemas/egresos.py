from pydantic import BaseModel, Field, validator, model_validator
from typing import Any, Optional, List
import datetime 
class Egreso (BaseModel):
    id: int = Field(ge="1" , title="Id del egreso")
    fecha: datetime.date = Field(title="Fecha del egreso")
    descripcion: Optional[str] = Field(default=None, title="Descripcion del egreso")
    valor: float = Field(lg=50, title="Valor del egreso")
    categoria: int = Field(title="Categoria del egreso")
    
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
                    "fecha": "2021-09-01",
                    "descripcion": "Pago de arriendo",
                    "valor": 100000,
                    "categoria": 1
                }
            }