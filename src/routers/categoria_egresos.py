from fastapi import APIRouter
from src.schemas.categoria_egresos import CategoriaEgresos
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from src.config.database import SessionLocal
from src.models.categoria_egreso import CategoriaEgreso as CategoriaEgresosModel
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from fastapi import status

router = APIRouter(prefix="/api/v1/categoria-egresos",tags=["categoria-egreso"])



@router.get("/", response_model=List[CategoriaEgresos], description="Obtener todas las categorias de egresos")
def obtener_categoria_egresos(offset: int = Query(default=None, min=0),limit: int = Query(default=None, min=1)
) -> List[CategoriaEgresos]:
    db = SessionLocal()
    query = db.query(CategoriaEgresosModel)
    if(offset is not None):
        query = query.offset(offset)
    if(limit is not None):
        query = query.limit(limit)
    result=query.all()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.get('/{id}', response_model=CategoriaEgresos, description="Obtener una categoria egreso por id")
def obtener_categoria_egreso(id: int = Path(ge=1)) -> CategoriaEgresos:
    db=SessionLocal()
    element=db.query(CategoriaEgresosModel).filter(CategoriaEgresosModel.id==id).first()
    if not element:
        return JSONResponse(content={"message": "The requested categoria egreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)


@router.post('/', response_model=CategoriaEgresos, description="Crear un egreso")
def crear_categoria_egreso(categoriaEgreso: CategoriaEgresos = Body()) -> dict:
    db=SessionLocal()
    new_categoria_egreso= CategoriaEgresosModel(**categoriaEgreso.model_dump())
    db.add(new_categoria_egreso)
    db.commit()
    return JSONResponse(content={"message": "Egreso registrado con exito", "data": jsonable_encoder(categoriaEgreso)}, status_code=status.HTTP_201_CREATED)

@router.put('/{id}', response_model=dict, description="Actualizar un egreso por id")
def update_categoria_egreso(id: int = Path(ge=1), categoria_egreso: CategoriaEgresos = Body()) -> dict:
    db=SessionLocal()
    element=db.query(CategoriaEgresosModel).filter(CategoriaEgresosModel.id==id).first()
    if not element:
        return JSONResponse(content={"message": "The requested categoria egreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    element.nombre = categoria_egreso.nombre
    element.descripcion = categoria_egreso.descripcion
    db.commit()
    return JSONResponse(content={"message": "The categoria egreso was successfully updated","data": jsonable_encoder(element)}, status_code=status.HTTP_200_OK)


@router.delete('/{id}', response_model=dict, description="Eliminar un egreso por id")
def eliminar_categoria_egreso(id: int = Path(ge=1)) -> dict:
    db=SessionLocal()
    element = db.query(CategoriaEgresosModel).filter(CategoriaEgresosModel.id == id).first()
    if not element:
        return JSONResponse(content={"message": "The requested categoria egreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    db.delete(element)
    db.commit()
    return JSONResponse(content={"message": "The categoria egreso was removed successfully","data": None}, status_code=status.HTTP_200_OK)
