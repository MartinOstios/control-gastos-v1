from fastapi import APIRouter
# from schemas.product import Product
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import JSONResponse
from typing import Any, Optional, List
from routers import egresos, ingresos, categoria_egresos, categoria_ingresos

router = APIRouter(prefix="/api/v1/reportes", tags=["reporte"])


@router.get('/basico', description="El reporte básico muestra cuántos ingresos se han recibido, cuántos egresos se han realizado y cuánto dinero se tiene actualmente (diferencia).")
def obtener_reporte_basico() -> dict:
    total_ingresos = sum([x["valor"] for x in ingresos.ingresos])
    total_egresos = sum([x["valor"] for x in egresos.egresos])
    diferencia = total_ingresos - total_egresos
    return JSONResponse(content={
        "ingresos": total_ingresos,
        "egresos": total_egresos,
        "dinero_actual": diferencia
    }, status_code=200)


@router.get('/ampliado', description="El reporte ampliado muestra la información de ingresos y egresos agrupada por categorías.")
def obtener_reporte_ampliado() -> dict:
    lista_ingresos = []


    for categoria_ingreso in categoria_ingresos.categorias_ingresos:
        movimientos = []
        for ingreso in ingresos.ingresos:
            if ingreso["categoria"] == categoria_ingreso["id"]:
                movimientos.append(ingreso)
        lista_ingresos.append({
            "categoria": categoria_ingreso["nombre"],
            "movimientos": movimientos
        })

    lista_egresos = []
    for categoria_egreso in categoria_egresos.categorias_egresos:
        movimientos = []
        for egreso in egresos.egresos:
            if egreso["categoria"] == categoria_egreso["id"]:
                movimientos.append(egreso)
        lista_egresos.append({
            "categoria": categoria_egreso["nombre"],
            "movimientos": movimientos
        })
        


    return JSONResponse(content={
        "ingresos": lista_ingresos,
        "egresos": lista_egresos
    })
