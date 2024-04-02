from fastapi import APIRouter
from schemas.egresos import Egreso
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
router = APIRouter(prefix="/api/v1/egresos", tags=["egreso"])

egresos = [
    {
        "id": 1,
        "fecha": "2021-09-01",
        "descripcion": "Pago de arriendo",
        "valor": 100000,
        "categoria": 1
    },
    {
        "id": 2,
        "fecha": "2021-09-02",
        "descripcion": "Pago de servicios",
        "valor": 50000,
        "categoria": 2
    },
    {
        "id": 3,
        "fecha": "2021-09-03",
        "descripcion": "Pago de hamburguesa",
        "valor": 12000,
        "categoria": 3
    }
]


@router.get("/", response_model=List[Egreso], description="Obtener todos los egresos")
def obtener_egresos() -> List[Egreso]:
    return JSONResponse(content=egresos, status_code=200)


@router.get('/{id}', response_model=Egreso, description="Obtener un egreso por id")
def obtener_egreso(id: int = Path(ge=1)) -> Egreso:
    for egreso in egresos:
        if egreso['id'] == id:
            return JSONResponse(content=egreso, status_code=200)
    return JSONResponse(content=None, status_code=404)


@router.post('/', response_model=Egreso, description="Crear un egreso")
def crear_egreso(egreso: Egreso = Body()) -> dict:
    egresos.append(jsonable_encoder(egreso))
    return JSONResponse(content={"message": "Egreso registrado con exito", "data": jsonable_encoder(egreso)}, status_code=201)


@router.delete('/{id}', response_model=dict, description="Eliminar un egreso por id")
def eliminar_egreso(id: int = Path(ge=1)) -> dict:
    for egreso in egresos:
        if egreso['id'] == id:
            egresos.remove(egreso)
            return JSONResponse(content={"message": "Egreso eliminado con exito", "data": egreso}, status_code=200)
    return JSONResponse(content={"message": "Egreso no encontrado", "data": None}, status_code=404)
