from fastapi import APIRouter
from src.schemas.ingresos import Ingreso
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from src.config.database import SessionLocal
from src.models.ingreso import Ingreso as IngresoModel
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from fastapi import status
from src.repositories.ingreso import IngresoRepository
router = APIRouter(prefix="/api/v1/ingresos", tags=["ingreso"])

from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends
from src.auth.has_access import security


@router.get("/", response_model=List[Ingreso], description="Obtener todos los ingresos")
def obtener_ingresos(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], offset: int = Query(default=None, min=0),limit: int = Query(default=None, min=1)
) -> List[Ingreso]:
    db = SessionLocal()
    result = IngresoRepository(db).obtener_ingresos(offset, limit)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.get('/{id}', response_model=Ingreso, description="Obtener un ingreso por id")
def obtener_ingreso(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> Ingreso:
    db=SessionLocal()
    element= IngresoRepository(db).obtener_ingreso(id)
    if not element:
        return JSONResponse(content={"message": "The requested ingreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)


@router.post('/', response_model=Ingreso, description="Crear un Ingreso")
def crear_ingreso(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], ingreso: Ingreso = Body()) -> dict:
    db=SessionLocal()
    new_ingreso= IngresoRepository(db).crear_ingreso(ingreso)
    return JSONResponse(content={"message": "ingreso registrado con exito", "data": jsonable_encoder(new_ingreso)}, status_code=status.HTTP_201_CREATED)

@router.put('/{id}', response_model=dict, description="Actualizar un ingreso por id")
def update_ingreso(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), ingreso: Ingreso = Body()) -> dict:
    db=SessionLocal()
    element= IngresoRepository(db).update_ingreso(id, ingreso)
    if not element:
        return JSONResponse(content={"message": "The requested ingreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "The ingreso was successfully updated","data": jsonable_encoder(element)}, status_code=status.HTTP_200_OK)


@router.delete('/{id}', response_model=dict, description="Eliminar un ingreso por id")
def eliminar_ingreso(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db=SessionLocal()
    element = IngresoRepository(db).eliminar_ingreso(id)
    if not element:
        return JSONResponse(content={"message": "The requested ingreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "The product was removed successfully","data": None}, status_code=status.HTTP_200_OK)
