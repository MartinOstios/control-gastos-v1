from fastapi import APIRouter
from src.schemas.ingresos import Ingreso
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
router = APIRouter(prefix="/api/v1/ingresos", tags=["ingreso"])

ingresos = [
    {
        "id": 1,
        "fecha": "2021-09-01",
        "descripcion": "Pago de nómina",
        "valor": 500000,
        "categoria": 1
    },
    {
        "id": 2,
        "fecha": "2021-09-02",
        "descripcion": "Pago de plata prestada a un amigo",
        "valor": 100000,
        "categoria": 2
    },
    {
        "id": 3,
        "fecha": "2021-09-03",
        "descripcion": "Pago de intereses de las cesantias",
        "valor": 30000,
        "categoria": 3
    }
]


@router.get("/", response_model=List[Ingreso], description="Obtener todos los ingresos")
def obtener_ingresos() -> List[Ingreso]:
    return JSONResponse(content=ingresos, status_code=200)


@router.get('/{id}', response_model=Ingreso, description="Obtener un ingreso por id")
def obtener_ingreso(id: int = Path(ge=1)) -> Ingreso:
    for ingreso in ingresos:
        if ingreso['id'] == id:
            return JSONResponse(content=ingreso, status_code=200)
    return JSONResponse(content=None, status_code=404)


@router.post('/', response_model=Ingreso, description="Crear un ingreso")
def crear_ingreso(ingreso: Ingreso = Body()) -> dict:
    ingresos.append(jsonable_encoder(ingreso))
    return JSONResponse(content={"message": "Ingreso registrado con exito", "data": jsonable_encoder(ingreso)}, status_code=201)


@router.delete('/{id}', response_model=dict, description="Eliminar un ingreso por id")
def eliminar_ingreso(id: int = Path(ge=1)) -> dict:
    for ingreso in ingresos:
        if ingreso['id'] == id:
            ingresos.remove(ingreso)
            return JSONResponse(content={"message": "Ingreso eliminado con exito", "data": ingreso}, status_code=200)
    return JSONResponse(content={"message": "Ingreso no encontrado", "data": None}, status_code=404)