from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.config.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(length=64), unique=True, index=True)
    nombre = Column(String(length=60))
    contraseña = Column(String(length=64))
    activo = Column(Boolean)
