# app/infrastructure/repositories/sql_product_repository.py
from app.infraestructure.utils.exceptions import ProductCreationError
from utils.db import SessionLocal
from app.domain.models.products import Product

class SQLProductRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self):
        return self.db.query(Product).all()

    def get_by_id(self, product_id):
        return self.db.query(Product).filter(Product.id == product_id).first()

   
    def save(self, product: Product):
        print(f"[DEBUG] Saving product: {product}")
        try:
            self.db.add(product)  # Solo crear
            self.db.commit()
            self.db.refresh(product)
            return product
        except Exception as e:
            self.db.rollback()
            print(f"[ERROR] Error saving product: {e}")
            raise


    def delete(self, product_id):
        product = self.get_by_id(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()
        return product
