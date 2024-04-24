from fastapi import APIRouter
# from schemas.product import Product
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import JSONResponse
from typing import Any, Optional, List
from src.models.ingreso import Ingreso as IngresoModel
from src.models.egreso import Egreso as EgresoModel
from src.models.categoria_egreso import CategoriaEgreso as CategoriaEgresoModel
from src.models.categoria_ingreso import CategoriaIngreso as CategoriaIngresoModel
from src.config.database import SessionLocal
from fastapi.encoders import jsonable_encoder


router = APIRouter(prefix="/api/v1/reportes", tags=["reporte"])


@router.get('/basico', description="El reporte básico muestra cuántos ingresos se han recibido, cuántos egresos se han realizado y cuánto dinero se tiene actualmente (diferencia).")
def obtener_reporte_basico() -> dict:
    db = SessionLocal()
    egresos = db.query(EgresoModel).all()
    ingresos = db.query(IngresoModel).all()

    total_ingresos = sum([x.valor for x in ingresos])
    total_egresos = sum([x.valor for x in egresos])
    print(total_egresos)
    diferencia = total_ingresos - total_egresos
    return JSONResponse(content={
        "ingresos": total_ingresos,
        "egresos": total_egresos,
        "dinero_actual": diferencia
    }, status_code=200)


@router.get('/ampliado', description="El reporte ampliado muestra la información de ingresos y egresos agrupada por categorías.")
def obtener_reporte_ampliado() -> dict:
    lista_ingresos = []
    db = SessionLocal()
    egresos = db.query(EgresoModel).all()
    ingresos = db.query(IngresoModel).all()
    categoria_ingresos = db.query(CategoriaIngresoModel).all()
    categoria_egresos = db.query(CategoriaEgresoModel).all()

    for categoria_ingreso in categoria_ingresos:

        movimientos = []

        for ingreso in ingresos:

            if ingreso.categoria_id == categoria_ingreso.id:

                movimientos.append(jsonable_encoder(ingreso))
        lista_ingresos.append({
            "categoria": categoria_ingreso.nombre,
            "movimientos": movimientos
        })

    lista_egresos = []
    for categoria_egreso in categoria_egresos:
        movimientos = []
        for egreso in egresos:
            if egreso.categoria_id == categoria_egreso.id:
                movimientos.append(jsonable_encoder(egreso))
        lista_egresos.append({
            "categoria": categoria_egreso.nombre,
            "movimientos": movimientos
        })

    return JSONResponse(content={
        "ingresos": lista_ingresos,
        "egresos": lista_egresos
    })
