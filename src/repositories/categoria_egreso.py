from typing import List
from src.schemas.categoria_egresos import CategoriaEgresos
from src.models.categoria_egreso import CategoriaEgreso as CategoriaEgresoModel

class CategoriaEgresoRepository():
    def __init__(self, db) -> None:
        self.db = db
        
    def obtener_categorias_egresos(self, offset: int , limit: int) -> List[CategoriaEgresos]:
        query = self.db.query(CategoriaEgresoModel)
        if(offset is not None):
            query = query.offset(offset)
        if(limit is not None):
            query = query.limit(limit)
        return query.all()
    
    def obtener_categoria_egreso(self, id: int) -> CategoriaEgresos:
        element=self.db.query(CategoriaEgresoModel).filter(CategoriaEgresoModel.id==id).first()
        return element
    
    def crear_categoria_egreso(self, categoria_egreso: CategoriaEgresos) -> dict:
        new_categoria_egreso= CategoriaEgresoModel(**categoria_egreso.model_dump())
        self.db.add(new_categoria_egreso)
        self.db.commit()
        self.db.refresh(new_categoria_egreso)
        return new_categoria_egreso
    
    def update_categoria_egreso(self, id: int, categoria_egreso: CategoriaEgresos) -> dict:
        element=self.db.query(CategoriaEgresoModel).filter(CategoriaEgresoModel.id==id).first()
        element.nombre = categoria_egreso.nombre
        element.descripcion = categoria_egreso.descripcion
        self.db.commit()
        return element
    
    def eliminar_categoria_egreso(self, id: int) -> dict:
        element = self.db.query(CategoriaEgresoModel).filter(CategoriaEgresoModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element