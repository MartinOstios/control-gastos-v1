from typing import List
from src.schemas.usuario import Usuario
from src.schemas.usuario import UsuarioCreado
from src.models.usuario import Usuario as UsuarioModel

class UsuarioRepository():
    def __init__(self, db) -> None:
        self.db = db
        
    def obtener_usuarios(self, offset: int , limit: int) -> List[Usuario]:
        query = self.db.query(UsuarioModel)
        if(offset is not None):
            query = query.offset(offset)
        if(limit is not None):
            query = query.limit(limit)
        return query.all()
    
    def obtener_usuario(self, id: int) -> Usuario:
        element=self.db.query(UsuarioModel).filter(UsuarioModel.id==id).first()
        return element
    
    def obtener_usuario(self, email: str) -> Usuario:
        element = self.db.query(UsuarioModel).filter(UsuarioModel.email ==email).first()
        return element
    
    def crear_usuario(self, usuario: UsuarioCreado) -> dict:
        new_user = UsuarioModel(**usuario.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def update_usuario(self, id: int, usuario: Usuario) -> dict:
        element=self.db.query(UsuarioModel).filter(UsuarioModel.id==id).first()
        element.email = usuario.email
        element.nombre = usuario.nombre
        element.contraseña = usuario.contraseña
        element.activo = usuario.activo
        self.db.commit()
        return element
    
    def eliminar_usuario(self, id: int) -> dict:
        element = self.db.query(UsuarioModel).filter(UsuarioModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element