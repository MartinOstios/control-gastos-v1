from fastapi import FastAPI
from src.routers import egresos, ingresos, categoria_egresos, categoria_ingresos, reportes
from src.middlewares.errorHandler import ErrorHandler


tags_metadata = [
    {
        "name": "egreso",
        "description": "Endpoints de la gestión de egresos",
    },
    {
        "name": "ingreso",
        "description": "Endpoints de la gestión de ingresos",
    },
    {
        "name": "categoria-egreso",
        "description": "Endpoints de la gestión de las categorías de egresos",
    },
    {
        "name": "categoria-ingreso",
        "description": "Endpoints de la gestión de las categorías de ingresos",
    },
    {
        "name": "reporte",
        "description": "Endpoints para obtener reportes"
    }
]
app = FastAPI(openapi_tags=tags_metadata)
app.include_router(egresos.router)
app.include_router(ingresos.router)
app.include_router(categoria_egresos.router)
app.include_router(categoria_ingresos.router)
app.include_router(reportes.router)
app.add_middleware(ErrorHandler)

app.title = "Control de gastos V1"
app.summary = "Control de gastos REST API con FastAPI"
app.description = "Esta es la API de una aplicación sencilla para el control de gastos"
app.version = "0.0.1"
app.contact = {
    "name": "Julian y Martin"
}
