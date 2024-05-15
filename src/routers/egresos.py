from fastapi import APIRouter
from src.schemas.egresos import Egreso
from src.repositories.egreso import EgresoRepository
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

from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends
from src.auth.has_access import security


@router.get("/", response_model=List[Egreso], description="Obtener todos los egresos")
def obtener_egresos(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], offset: int = Query(default=None, min=0), limit: int = Query(default=None, min=1)
                    ) -> List[Egreso]:
    db = SessionLocal()
    result = EgresoRepository(db).obtener_egresos(offset, limit)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.get('/{id}', response_model=Egreso, description="Obtener un egreso por id")
def obtener_egreso(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> Egreso:
    db = SessionLocal()
    element = EgresoRepository(db).obtener_egreso(id)
    if not element:
        return JSONResponse(content={"message": "The requested egreso was not found", "data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)


@router.post('/', response_model=Egreso, description="Crear un egreso")
def crear_egreso(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], egreso: Egreso = Body()) -> dict:
    db = SessionLocal()
    nuevo_egreso = EgresoRepository(db).crear_egreso(egreso)
    return JSONResponse(content={"message": "Egreso registrado con exito", "data": jsonable_encoder(nuevo_egreso)}, status_code=status.HTTP_201_CREATED)


@router.put('/{id}', response_model=dict, description="Actualizar un egreso por id")
def update_egreso(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), egreso: Egreso = Body()) -> dict:
    db = SessionLocal()
    element = EgresoRepository(db).obtener_egreso(id)
    if not element:
        return JSONResponse(content={"message": "The requested egreso was not found", "data": None}, status_code=status.HTTP_404_NOT_FOUND)

    element = EgresoRepository(db).actualizar_egreso(id, egreso)
    return JSONResponse(content={"message": "The egreso was successfully updated", "data": jsonable_encoder(element)}, status_code=status.HTTP_200_OK)


@router.delete('/{id}', response_model=dict, description="Eliminar un egreso por id")
def eliminar_egreso(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = EgresoRepository(db).obtener_egreso(id)
    if not element:
        return JSONResponse(content={"message": "The requested egreso was not found", "data": None}, status_code=status.HTTP_404_NOT_FOUND)
    
    EgresoRepository(db).eliminar_egreso(id)
    return JSONResponse(content={"message": "The product wass removed successfully", "data": None}, status_code=status.HTTP_200_OK)
