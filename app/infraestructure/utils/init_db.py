from app.infraestructure.utils.db import engine
from app.infraestructure.utils.tables import Base
import app.domain.models.products as products

Base.metadata.create_all(bind=engine, checkfirst=True, tables=[products.Product.__table__])
