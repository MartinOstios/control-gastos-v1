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
from src.repositories.categoria_egreso import CategoriaEgresoRepository

router = APIRouter(prefix="/api/v1/categoria-egresos",tags=["categoria-egreso"])



@router.get("/", response_model=List[CategoriaEgresos], description="Obtener todas las categorias de egresos")
def obtener_categoria_egresos(offset: int = Query(default=None, min=0),limit: int = Query(default=None, min=1)
) -> List[CategoriaEgresos]:
    db = SessionLocal()
    result=CategoriaEgresoRepository(db).obtener_categorias_egresos(offset, limit)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.get('/{id}', response_model=CategoriaEgresos, description="Obtener una categoria egreso por id")
def obtener_categoria_egreso(id: int = Path(ge=1)) -> CategoriaEgresos:
    db=SessionLocal()
    element=CategoriaEgresoRepository(db).obtener_categoria_egreso(id)
    if not element:
        return JSONResponse(content={"message": "The requested categoria egreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)


@router.post('/', response_model=CategoriaEgresos, description="Crear un egreso")
def crear_categoria_egreso(categoriaEgreso: CategoriaEgresos = Body()) -> dict:
    db=SessionLocal()
    new_categoria_egreso= CategoriaEgresoRepository(db).crear_categoria_egreso(categoriaEgreso)
    return JSONResponse(content={"message": "Egreso registrado con exito", "data": jsonable_encoder(new_categoria_egreso)}, status_code=status.HTTP_201_CREATED)

@router.put('/{id}', response_model=dict, description="Actualizar un egreso por id")
def update_categoria_egreso(id: int = Path(ge=1), categoria_egreso: CategoriaEgresos = Body()) -> dict:
    db=SessionLocal()
    element= CategoriaEgresoRepository(db).update_categoria_egreso(id, categoria_egreso)
    if not element:
        return JSONResponse(content={"message": "The requested categoria egreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "The categoria egreso was successfully updated","data": jsonable_encoder(element)}, status_code=status.HTTP_200_OK)


@router.delete('/{id}', response_model=dict, description="Eliminar un egreso por id")
def eliminar_categoria_egreso(id: int = Path(ge=1)) -> dict:
    db=SessionLocal()
    element = CategoriaEgresoRepository(db).eliminar_categoria_egreso(id)
    if not element:
        return JSONResponse(content={"message": "The requested categoria egreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "The categoria egreso was removed successfully","data": None}, status_code=status.HTTP_200_OK)
