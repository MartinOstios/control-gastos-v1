from fastapi import HTTPException, status
from src.repositories.usuario import UsuarioRepository
from src.config.database import SessionLocal
from src.auth import auth_handler
from src.schemas.usuario import UsuarioLogin as UserLoginSchema
from src.schemas.usuario import UsuarioCreado as UserCreateSchema

class AuthRepository:
    def __init__(self) -> None:
        pass
    
    def register_user(self,user: UserCreateSchema) -> dict:
        db = SessionLocal()
        if UsuarioRepository(db).obtener_usuario(email=user.email) != None:
            raise Exception("Account already exists")
        hashed_password = auth_handler.hash_password(password=user.contraseña)
        new_user: UserCreateSchema = UserCreateSchema(nombre=user.nombre,email=user.email,contraseña=hashed_password,activo=True)
        return UsuarioRepository(db).crear_usuario(new_user)

    def login_user(self, user: UserLoginSchema) -> dict:
        db = SessionLocal()
        check_user = UsuarioRepository(db).obtener_usuario(email=user.email)
        if check_user is None:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials (1)")
        if not check_user.activo:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="The user is not allowed to log in")
        if not auth_handler.verify_password(user.contraseña, check_user.contraseña):
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials (2)")
        access_token = auth_handler.encode_token(check_user)
        refresh_token = auth_handler.encode_refresh_token(check_user)
        
        return access_token, refresh_token


