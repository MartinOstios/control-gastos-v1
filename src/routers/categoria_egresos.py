from fastapi import APIRouter
from src.schemas.categoria_egresos import CategoriaEgresos
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List

router = APIRouter(prefix="/api/v1/categoria-egresos",
                   tags=["categoria-egreso"])

categorias_egresos = [
    {
        "id": 1,
        "nombre": "Arriendo",
        "descripcion": "Pago de arriendo"
    },
    {
        "id": 2,
        "nombre": "Servicios",
        "descripcion": "Pago de servicios"
    },
    {
        "id": 3,
        "nombre": "Alimentación",
        "descripcion": "Gastos en comida"
    }
]


@router.get('/', response_model=List[CategoriaEgresos], description="Obtener todas las categorías de egreso")
def obtener_categorias() -> List[CategoriaEgresos]:
    return JSONResponse(content=categorias_egresos, status_code=200)


@router.get('/{id}', response_model=List[CategoriaEgresos], description="Obtener todas las categorías de egreso")
def obtener_categoria(id: int = Path(ge=1)) -> CategoriaEgresos:
    for categoria in categorias_egresos:
        if categoria['id'] == id:
            return JSONResponse(content=categoria, status_code=200)
    return JSONResponse(content=None, status_code=404)


@router.post('/',  response_model=CategoriaEgresos, description="Crear una categoria egreso")
def crear_categoria(categoria: CategoriaEgresos = Body()) -> dict:
    categorias_egresos.append(categoria.model_dump())
    return JSONResponse(content={"message": "Egreso registrado con exito", "data": categoria.model_dump()}, status_code=201)

@router.delete('/{id}', response_model=dict, description="Eliminar un egreso por id")
def eliminar_categoria(id: int = Path(ge=1)) -> dict:
    for categoria in categorias_egresos:
        if categoria['id'] == id:
            categorias_egresos.remove(categoria)
            return JSONResponse(content={"message": "Egreso eliminado con exito", "data": categoria}, status_code=200)
    return JSONResponse(content={"message": "Egreso no encontrado", "data": None}, status_code=404)