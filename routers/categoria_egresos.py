from fastapi import APIRouter
from schemas.categoria_egresos import CategoriaEgresos
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List

router = APIRouter()

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

@router.post('/categorias-egresos',tags=['categorias-egresos'],response_model=CategoriaEgresos,description="Crear una categoria egreso")
def crear_categoria_egreso(categoria: CategoriaEgresos = Body()) -> dict:
    categorias_egresos.append(categoria.model_dump())
    return JSONResponse(content={"message": "Egreso registrado con exito","data": categoria.model_dump()}, status_code=201)
