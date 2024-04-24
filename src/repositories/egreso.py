from typing import List
from src.schemas.egresos import Egreso
from src.models.egreso import Egreso as EgresoModel


class EgresoRepository():
    def __init__(self, db) -> None:
        self.db = db

    def obtener_egresos(self, offset: int, limit: int) -> List[Egreso]:
        query = self.db.query(EgresoModel)
        if (offset is not None):
            query = query.offset(offset)
        if (limit is not None):
            query = query.limit(limit)
        return query.all()

    def obtener_egreso(self, id: int) -> Egreso:
        element = self.db.query(EgresoModel).filter(
            EgresoModel.id == id).first()
        return element

    def crear_egreso(self, egreso: Egreso) -> dict:
        nuevo_egreso = EgresoModel(**egreso.model_dump())
        self.db.add(nuevo_egreso)
        self.db.commit()
        self.db.refresh(nuevo_egreso)
        return nuevo_egreso

    def actualizar_egreso(self, id: int, egreso: Egreso) -> dict:
        element = self.db.query(EgresoModel).filter(
            EgresoModel.id == id).first()

        element.fecha = egreso.fecha
        element.descripcion = egreso.descripcion
        element.valor = egreso.valor
        element.categoria_id = egreso.categoria_id

        self.db.commit()
        self.db.refresh(element)

        return element

    def eliminar_egreso(self, id: int) -> dict:
        element: Egreso = self.db.query(EgresoModel).filter(
            EgresoModel.id == id).first()

        self.db.delete(element)
        self.db.commit()

        return element