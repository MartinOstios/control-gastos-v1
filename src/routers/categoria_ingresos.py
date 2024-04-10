from fastapi import APIRouter
from src.schemas.categoria_ingresos import CategoriaIngresos
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from src.config.database import SessionLocal
from src.models.categoria_ingreso import CategoriaIngreso as CategoriaIngresosModel
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from fastapi import status
router = APIRouter(prefix="/api/v1/categoria-ingresos",tags=["categoria-ingreso"])


@router.get("/", response_model=List[CategoriaIngresos], description="Obtener todas las categorias de ingresos")
def obtener_categoria_ingresos(offset: int = Query(default=None, min=0),limit: int = Query(default=None, min=1)
) -> List[CategoriaIngresos]:
    db = SessionLocal()
    query = db.query(CategoriaIngresosModel)
    if(offset is not None):
        query = query.offset(offset)
    if(limit is not None):
        query = query.limit(limit)
    result=query.all()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.get('/{id}', response_model=CategoriaIngresos, description="Obtener una categoria ingreso por id")
def obtener_categoria_ingreso(id: int = Path(ge=1)) -> CategoriaIngresos:
    db=SessionLocal()
    element=db.query(CategoriaIngresosModel).filter(CategoriaIngresosModel.id==id).first()
    if not element:
        return JSONResponse(content={"message": "The requested categoria ingreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)


@router.post('/', response_model=CategoriaIngresos, description="Crear un ingreso")
def crear_categoria_ingreso(categoriaIngreso: CategoriaIngresos = Body()) -> dict:
    db=SessionLocal()
    new_categoria_ingreso= CategoriaIngresosModel(**categoriaIngreso.model_dump())
    db.add(new_categoria_ingreso)
    db.commit()
    return JSONResponse(content={"message": "Categoria ingreso registrado con exito", "data": jsonable_encoder(categoriaIngreso)}, status_code=status.HTTP_201_CREATED)

@router.put('/{id}', response_model=dict, description="Actualizar un ingreso por id")
def update_categoria_ingreso(id: int = Path(ge=1), categoria_ingreso: CategoriaIngresos = Body()) -> dict:
    db=SessionLocal()
    element=db.query(CategoriaIngresosModel).filter(CategoriaIngresosModel.id==id).first()
    if not element:
        return JSONResponse(content={"message": "The requested categoria ingreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    element.name = categoria_ingreso.name
    element.price = categoria_ingreso.price
    element.expiration = categoria_ingreso.expiration
    db.commit()
    return JSONResponse(content={"message": "The categoria ingreso was successfully updated","data": jsonable_encoder(element)}, status_code=status.HTTP_200_OK)


@router.delete('/{id}', response_model=dict, description="Eliminar un ingreso por id")
def eliminar_categoria_ingreso(id: int = Path(ge=1)) -> dict:
    db=SessionLocal()
    element = db.query(CategoriaIngresosModel).filter(CategoriaIngresosModel.id == id).first()
    if not element:
        return JSONResponse(content={"message": "The requested categoria ingreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    db.delete(element)
    db.commit()
    return JSONResponse(content={"message": "The categoria ingreso was removed successfully","data": None}, status_code=status.HTTP_200_OK)
