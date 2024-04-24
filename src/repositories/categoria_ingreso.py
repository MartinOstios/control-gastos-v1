from typing import List
from src.schemas.categoria_ingresos import CategoriaIngresos
from src.models.categoria_ingreso import CategoriaIngreso as CategoriaIngresoModel

class CategoriaIngresoRepository():
    def __init__(self, db) -> None:
        self.db = db
        
    def obtener_categorias_ingresos(self, offset: int , limit: int) -> List[CategoriaIngresos]:
        query = self.db.query(CategoriaIngresoModel)
        if(offset is not None):
            query = query.offset(offset)
        if(limit is not None):
            query = query.limit(limit)
        return query.all()
    
    def obtener_categoria_ingreso(self, id: int) -> CategoriaIngresos:
        element=self.db.query(CategoriaIngresoModel).filter(CategoriaIngresoModel.id==id).first()
        return element
    
    def crear_categoria_ingreso(self, categoria_ingreso: CategoriaIngresos) -> dict:
        new_categoria_ingreso= CategoriaIngresoModel(**categoria_ingreso.model_dump())
        self.db.add(new_categoria_ingreso)
        self.db.commit()
        self.db.refresh(new_categoria_ingreso)
        return new_categoria_ingreso
    
    def update_categoria_ingreso(self, id: int, categoria_ingreso: CategoriaIngresos) -> dict:
        element=self.db.query(CategoriaIngresoModel).filter(CategoriaIngresoModel.id==id).first()
        element.nombre = categoria_ingreso.nombre
        element.descripcion = categoria_ingreso.descripcion
        self.db.commit()
        return element
    
    def eliminar_categoria_ingreso(self, id: int) -> dict:
        element = self.db.query(CategoriaIngresoModel).filter(CategoriaIngresoModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element