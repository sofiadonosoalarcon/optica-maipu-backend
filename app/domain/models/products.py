from sqlalchemy import Column, BigInteger, String, Integer
from app.infraestructure.utils.tables import Base

class Product(Base):
    __tablename__ = 'producto'
    id = Column(BigInteger, primary_key=True, autoincrement=True) 
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(300), nullable=False)
    precio_unitario = Column(BigInteger, nullable=False)
    stock = Column(Integer, nullable=False)
