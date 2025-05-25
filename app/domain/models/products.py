from sqlalchemy import Column, BigInteger, String, Integer, Numeric, DateTime, CHAR
from app.infraestructure.utils.tables import Base
from datetime import datetime

class Product(Base):
    __tablename__ = 'producto'

    producto_id = Column(BigInteger, primary_key=True, autoincrement=True)  # Añadir autoincrement
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(300), nullable=False)
    stock = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric, nullable=False)  # Numeric para precios
    estado = Column(CHAR(1), nullable=False, default='A')
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)  # Fecha de creación

    def __repr__(self):
        return f"<Product(nombre={self.nombre}, precio_unitario={self.precio_unitario}, stock={self.stock}, estado={self.estado})>"
