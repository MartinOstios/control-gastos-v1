from fastapi import FastAPI
from routers import egresos, ingresos, categoria_egresos, categoria_ingresos


tags_metadata = [
    {
        "name": "web",
        "description": "Endpoints of example",
    },
    {
        "name": "products",
        "description": "Product handling endpoints",
    },
]
app = FastAPI(openapi_tags=tags_metadata)
app.include_router(egresos.router)
app.include_router(ingresos.router)
app.include_router(categoria_egresos.router)
app.include_router(categoria_ingresos.router)


app.title = "Gastos API"
app.summary = "Gastos REST API whit FastAPI"
app.description = "This is a simple API to manage the expenses."
app.version = "0.0.1"
app.contact = {
    "name": "Julian y Martin"
}