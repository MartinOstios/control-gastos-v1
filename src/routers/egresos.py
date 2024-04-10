from fastapi import APIRouter
from src.schemas.egresos import Egreso
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from src.config.database import SessionLocal
from src.models.egreso import Egreso as EgresoModel
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from fastapi import status
router = APIRouter(prefix="/api/v1/egresos", tags=["egreso"])


@router.get("/", response_model=List[Egreso], description="Obtener todos los egresos")
def obtener_egresos(offset: int = Query(default=None, min=0),limit: int = Query(default=None, min=1)
) -> List[Egreso]:
    db = SessionLocal()
    query = db.query(EgresoModel)
    if(offset is not None):
        query = query.offset(offset)
    if(limit is not None):
        query = query.limit(limit)
    result=query.all()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.get('/{id}', response_model=Egreso, description="Obtener un egreso por id")
def obtener_egreso(id: int = Path(ge=1)) -> Egreso:
    db=SessionLocal()
    element=db.query(EgresoModel).filter(EgresoModel.id==id).first()
    if not element:
        return JSONResponse(content={"message": "The requested egreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)


@router.post('/', response_model=Egreso, description="Crear un egreso")
def crear_egreso(egreso: Egreso = Body()) -> dict:
    db=SessionLocal()
    new_egreso= EgresoModel(**egreso.model_dump())
    db.add(new_egreso)
    db.commit()
    return JSONResponse(content={"message": "Egreso registrado con exito", "data": jsonable_encoder(egreso)}, status_code=status.HTTP_201_CREATED)

@router.put('/{id}', response_model=dict, description="Actualizar un egreso por id")
def update_egreso(id: int = Path(ge=1), egreso: Egreso = Body()) -> dict:
    db=SessionLocal()
    element=db.query(EgresoModel).filter(EgresoModel.id==id).first()
    if not element:
        return JSONResponse(content={"message": "The requested egreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    element.fecha = egreso.fecha
    element.descripcion = egreso.descripcion
    element.valor = egreso.valor
    element.categoria_id = egreso.categoria_id
    db.commit()
    return JSONResponse(content={"message": "The egreso was successfully updated","data": jsonable_encoder(element)}, status_code=status.HTTP_200_OK)


@router.delete('/{id}', response_model=dict, description="Eliminar un egreso por id")
def eliminar_egreso(id: int = Path(ge=1)) -> dict:
    db=SessionLocal()
    element = db.query(EgresoModel).filter(EgresoModel.id == id).first()
    if not element:
        return JSONResponse(content={"message": "The requested egreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    db.delete(element)
    db.commit()
    return JSONResponse(content={"message": "The product wass removed successfully","data": None}, status_code=status.HTTP_200_OK)
