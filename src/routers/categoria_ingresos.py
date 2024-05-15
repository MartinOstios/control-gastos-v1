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
from src.repositories.categoria_ingreso import CategoriaIngresoRepository
router = APIRouter(prefix="/api/v1/categoria-ingresos",tags=["categoria-ingreso"])


from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends
from src.auth.has_access import security


@router.get("/", response_model=List[CategoriaIngresos], description="Obtener todas las categorias de ingresos")
def obtener_categoria_ingresos(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], offset: int = Query(default=None, min=0),limit: int = Query(default=None, min=1)
) -> List[CategoriaIngresos]:
    db = SessionLocal()
    result = CategoriaIngresoRepository(db).obtener_categorias_ingresos(offset, limit)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.get('/{id}', response_model=CategoriaIngresos, description="Obtener una categoria ingreso por id")
def obtener_categoria_ingreso(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> CategoriaIngresos:
    db=SessionLocal()
    element= CategoriaIngresoRepository(db).obtener_categoria_ingreso(id)
    if not element:
        return JSONResponse(content={"message": "The requested categoria ingreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)


@router.post('/', response_model=CategoriaIngresos, description="Crear un ingreso")
def crear_categoria_ingreso(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], categoriaIngreso: CategoriaIngresos = Body()) -> dict:
    db=SessionLocal()
    new_categoria_ingreso= CategoriaIngresoRepository(db).crear_categoria_ingreso(categoriaIngreso)
    return JSONResponse(content={"message": "Categoria ingreso registrado con exito", "data": jsonable_encoder(new_categoria_ingreso)}, status_code=status.HTTP_201_CREATED)

@router.put('/{id}', response_model=dict, description="Actualizar un ingreso por id")
def update_categoria_ingreso(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), categoria_ingreso: CategoriaIngresos = Body()) -> dict:
    db=SessionLocal()
    element= CategoriaIngresoRepository(db).update_categoria_ingreso(id, categoria_ingreso)
    if not element:
        return JSONResponse(content={"message": "The requested categoria ingreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "The categoria ingreso was successfully updated","data": jsonable_encoder(element)}, status_code=status.HTTP_200_OK)


@router.delete('/{id}', response_model=dict, description="Eliminar un ingreso por id")
def eliminar_categoria_ingreso(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db=SessionLocal()
    element = CategoriaIngresoRepository(db).eliminar_categoria_ingreso(id)
    if not element:
        return JSONResponse(content={"message": "The requested categoria ingreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "The categoria ingreso was removed successfully","data": None}, status_code=status.HTTP_200_OK)
