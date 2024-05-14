from fastapi import FastAPI
from src.routers import egresos, ingresos, categoria_egresos, categoria_ingresos, reportes, usuario
from src.middlewares.errorHandler import ErrorHandler
from src.config.database import Base, engine
from src.models.categoria_egreso import CategoriaEgreso
from src.models.categoria_ingreso import CategoriaIngreso
from src.models.egreso import Egreso
from src.models.ingreso import Ingreso
from src.models.usuario import Usuario
from src.routers.auth import auth_router

Base.metadata.create_all(bind=engine)


tags_metadata = [
    {
        "name": "usuario",
        "description": "Endpoints para la gestión deu suarios"
    },
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
    },
    {
    "name": "auth",
    "description": "User's authentication",
    },

]
app = FastAPI(openapi_tags=tags_metadata)
app.include_router(egresos.router)
app.include_router(ingresos.router)
app.include_router(categoria_egresos.router)
app.include_router(categoria_ingresos.router)
app.include_router(reportes.router)
app.include_router(usuario.router)
app.include_router(prefix="", router=auth_router)
app.add_middleware(ErrorHandler)

app.title = "Control de gastos V1"
app.summary = "Control de gastos REST API con FastAPI"
app.description = "Esta es la API de una aplicación sencilla para el control de gastos"
app.version = "0.0.1"
app.contact = {
    "name": "Julian y Martin"
}
