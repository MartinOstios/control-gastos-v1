from typing import List
from src.schemas.ingresos import Ingreso
from src.models.ingreso import Ingreso as IngresoModel

class IngresoRepository():
    def __init__(self, db) -> None:
        self.db = db
        
    def obtener_ingresos(self, offset: int , limit: int) -> List[Ingreso]:
        query = self.db.query(IngresoModel)
        if(offset is not None):
            query = query.offset(offset)
        if(limit is not None):
            query = query.limit(limit)
        return query.all()

    def obtener_ingreso(self, id: int) -> Ingreso:
        element=self.db.query(IngresoModel).filter(IngresoModel.id==id).first()
        return element
    
    def crear_ingreso(self, ingreso: Ingreso) -> dict:
        new_ingreso= IngresoModel(**ingreso.model_dump())
        self.db.add(new_ingreso)
        self.db.commit()
        self.db.refresh(new_ingreso)
        return new_ingreso
    
    def update_ingreso(self, id: int, ingreso: Ingreso) -> dict:
        element=self.db.query(IngresoModel).filter(IngresoModel.id==id).first()
        element.fecha = ingreso.fecha
        element.descripcion = ingreso.descripcion
        element.valor = ingreso.valor
        element.categoria_id = ingreso.categoria_id
        self.db.commit()
        return element
    
    def eliminar_ingreso(self, id: int) -> dict:
        element = self.db.query(IngresoModel).filter(IngresoModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element
