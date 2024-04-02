# Programa para control de gastos (V1)

## Integrantes
- Julián Andrés Veloza
- Martín Ostios Arias


## Endpoints

### Egresos
| Verbo | URI | Descripción |
|----------|----------|----------|
| GET | /api/v1/egresos  | Obtener todos los egresos  |
| GET | /api/v1/egresos/:id | Obtener un egreso |
| POST | /api/v1/egresos | Crear un egreso |
| DELETE | /apI/v1/egresos/:id | Eliminar un egreso |

### Ingresos
| Verbo | URI | Descripción |
|----------|----------|----------|
| GET | /api/v1/ingresos  | Obtener todos los ingresos  |
| GET | /api/v1/ingresos/:id | Obtener un ingreso |
| POST | /api/v1/ingresos | Crear un ingreso |
| DELETE | /apI/v1/ingresos/:id | Eliminar un ingreso |

### Categorías de egresos
| Verbo | URI | Descripción |
|----------|----------|----------|
| GET | /api/v1/categoria-egresos  | Obtener todos las categorias de egresos |
| GET | /api/v1/categoria-egresos/:id | Obtener una categoria de egreso |
| POST | /api/v1/categoria-egresos | Crear un categoria de egreso |
| DELETE | /apI/v1/categoria-egresos/:id | Eliminar un categoria de egreso |


### Categorías de ingresos
| Verbo | URI | Descripción |
|----------|----------|----------|
| GET | /api/v1/categoria-ingresos  | Obtener todos las categorias de ingresos |
| GET | /api/v1/categoria-ingresos/:id | Obtener una categoria de ingreso |
| POST | /api/v1/categoria-ingresos | Crear un categoria de ingreso |
| DELETE | /apI/v1/categoria-ingresos/:id | Eliminar un categoria de ingreso |

### Reportes
| Verbo | URI | Descripción |
|----------|----------|----------|
| GET | /api/v1/reportes/basico  | Obtener un reporte en donde está: total de ingresos, total de egresos y dinero actual |
| GET | /api/v1/reportes/ampliado | Obtener reporte de ingresos y egresos agrupados por sus respectivas categorías |