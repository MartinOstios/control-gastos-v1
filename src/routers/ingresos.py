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
def obtener_ingresos(offset: int = Query(default=None, min=0),limit: int = Query(default=None, min=1)
) -> List[Ingreso]:
    db = SessionLocal()
    query = db.query(IngresoModel)
    if(offset is not None):
        query = query.offset(offset)
    if(limit is not None):
        query = query.limit(limit)
    result=query.all()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.get('/{id}', response_model=Ingreso, description="Obtener un ingreso por id")
def obtener_ingreso(id: int = Path(ge=1)) -> Ingreso:
    db=SessionLocal()
    element=db.query(IngresoModel).filter(IngresoModel.id==id).first()
    if not element:
        return JSONResponse(content={"message": "The requested ingreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)


@router.post('/', response_model=Ingreso, description="Crear un Ingreso")
def crear_ingreso(ingreso: Ingreso = Body()) -> dict:
    db=SessionLocal()
    new_ingreso= IngresoModel(**ingreso.model_dump())
    db.add(new_ingreso)
    db.commit()
    return JSONResponse(content={"message": "ingreso registrado con exito", "data": jsonable_encoder(ingreso)}, status_code=status.HTTP_201_CREATED)

@router.put('/{id}', response_model=dict, description="Actualizar un ingreso por id")
def update_ingreso(id: int = Path(ge=1), ingreso: Ingreso = Body()) -> dict:
    db=SessionLocal()
    element=db.query(IngresoModel).filter(IngresoModel.id==id).first()
    if not element:
        return JSONResponse(content={"message": "The requested ingreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    element.fecha = ingreso.fecha
    element.descripcion = ingreso.descripcion
    element.valor = ingreso.valor
    element.categoria_id = ingreso.categoria_id
    db.commit()
    return JSONResponse(content={"message": "The ingreso was successfully updated","data": jsonable_encoder(element)}, status_code=status.HTTP_200_OK)


@router.delete('/{id}', response_model=dict, description="Eliminar un ingreso por id")
def eliminar_ingreso(id: int = Path(ge=1)) -> dict:
    db=SessionLocal()
    element = db.query(IngresoModel).filter(IngresoModel.id == id).first()
    if not element:
        return JSONResponse(content={"message": "The requested ingreso was not found","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    db.delete(element)
    db.commit()
    return JSONResponse(content={"message": "The product was removed successfully","data": None}, status_code=status.HTTP_200_OK)
