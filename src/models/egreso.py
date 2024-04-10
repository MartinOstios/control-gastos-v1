from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from src.config.database import Base

class Egreso(Base):
    __tablename__ = "egresos"

    id          = Column(Integer, primary_key=True, autoincrement=True)
    fecha       = Column(Date)
    descripcion = Column(String(length=200))
    valor       = Column(Integer)
    categoria_id = Column(Integer, ForeignKey("categoria_egresos.id"))

    categoria   = relationship("CategoriaEgreso", back_populates="egresos")
