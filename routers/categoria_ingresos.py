from fastapi import APIRouter
from schemas.categoria_ingresos import CategoriaIngresos
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List

router = APIRouter(prefix="/api/v1/categoria-ingresos",
                   tags=["categoria-ingreso"])

categorias_ingresos = [
    {
        "id": 1,
        "nombre": "Trabajo",
        "descripcion": "Pago de nómina"
    },
    {
        "id": 2,
        "nombre": "Prestamos",
        "descripcion": "Plata prestada a otras personas"
    },
    {
        "id": 3,
        "nombre": "Otros",
        "descripcion": "Otros tipos de entradas"
    }
]


@router.get('/', response_model=List[CategoriaIngresos], description="Obtener todas las categorías de ingreso")
def obtener_categorias() -> List[CategoriaIngresos]:
    return JSONResponse(content=categorias_ingresos, status_code=200)


@router.get('/{id}', response_model=List[CategoriaIngresos], description="Obtener todas las categorías de ingreso")
def obtener_categoria(id: int = Path(ge=1)) -> CategoriaIngresos:
    for categoria in categorias_ingresos:
        if categoria['id'] == id:
            return JSONResponse(content=categoria, status_code=200)
    return JSONResponse(content=None, status_code=404)


@router.post('/',  response_model=CategoriaIngresos, description="Crear una categoria ingreso")
def crear_categoria(categoria: CategoriaIngresos = Body()) -> dict:
    categorias_ingresos.append(categoria.model_dump())
    return JSONResponse(content={"message": "ingreso registrado con exito", "data": categoria.model_dump()}, status_code=201)

@router.delete('/{id}', response_model=dict, description="Eliminar un ingreso por id")
def eliminar_categoria(id: int = Path(ge=1)) -> dict:
    for categoria in categorias_ingresos:
        if categoria['id'] == id:
            categorias_ingresos.remove(categoria)
            return JSONResponse(content={"message": "ingreso eliminado con exito", "data": categoria}, status_code=200)
    return JSONResponse(content={"message": "ingreso no encontrado", "data": None}, status_code=404)