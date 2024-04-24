from fastapi import APIRouter
from src.schemas.usuario import Usuario
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from src.config.database import SessionLocal
from src.models.usuario import Usuario as UsuarioModel
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from fastapi import status
from src.repositories.usuario import UsuarioRepository
router = APIRouter(prefix="/api/v1/usuarios", tags=["usuario"])


@router.get("/", response_model=List[Usuario], description="Obtener todos los usuarios")
def obtener_usuarios(offset: int = Query(default=None, min=0),limit: int = Query(default=None, min=1)
) -> List[Usuario]:
    db = SessionLocal()
    result = UsuarioRepository(db).obtener_usuarios(offset, limit)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.get('/{id}', response_model=Usuario, description="Obtener un usuario por id")
def obtener_usuario(id: int = Path(ge=1)) -> Usuario:
    db=SessionLocal()
    element= UsuarioRepository(db).obtener_usuario(id)
    if not element:
        return JSONResponse(content={"message": "El usuario no fue encontrado","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)


@router.post('/', response_model=Usuario, description="Crear un usuario")
def crear_usuario(usuario: Usuario = Body()) -> dict:
    db=SessionLocal()
    new_usuario= UsuarioRepository(db).crear_usuario(usuario)
    return JSONResponse(content={"message": "Usuario registrado con exito", "data": jsonable_encoder(new_usuario)}, status_code=status.HTTP_201_CREATED)

@router.put('/{id}', response_model=dict, description="Actualizar un usuario por id")
def update_usuario(id: int = Path(ge=1), usuario: Usuario = Body()) -> dict:
    db=SessionLocal()
    element= UsuarioRepository(db).update_usuario(id, usuario)
    if not element:
        return JSONResponse(content={"message": "El usuario no fue encontrado","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "El usuario se actualizó correctamente","data": jsonable_encoder(element)}, status_code=status.HTTP_200_OK)


@router.delete('/{id}', response_model=dict, description="Eliminar un usuario por id")
def eliminar_usuario(id: int = Path(ge=1)) -> dict:
    db=SessionLocal()
    element = UsuarioRepository(db).eliminar_usuario(id)
    if not element:
        return JSONResponse(content={"message": "El usuario no fue encontrado","data": None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message": "El usuario se eliminó correctamente","data": None}, status_code=status.HTTP_200_OK)
