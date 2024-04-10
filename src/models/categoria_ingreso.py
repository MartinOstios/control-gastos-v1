from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.config.database import Base


class CategoriaIngreso(Base):
    __tablename__ = "categoria_ingresos"
    
    id          = Column(Integer, primary_key=True, autoincrement=True)
    nombre      = Column(String(length=50), unique=True)
    descripcion = Column(String(length=200))

    ingresos = relationship("Ingreso", back_populates="categoria")
