# from app.domain.models.products import Product  
# from sqlalchemy.orm import Session

# class SQLProductRepository:
#     def __init__(self, db_session: Session):
#         self.db = db_session

#     def get_all(self):
#         return self.db.query(Product).all()

#     def get_by_id(self, product_id: int):
#         return self.db.query(Product).filter_by(producto_id=product_id).first()

#     def save(self, product: Product):
#         if product.producto_id:
#             existing = self.get_by_id(product.producto_id)
#             if existing:
#                 existing.nombre = product.nombre
#                 existing.descripcion = product.descripcion
#                 existing.precio_unitario = product.precio_unitario
#                 existing.stock = product.stock
#                 self.db.commit()
#                 self.db.refresh(existing)
#                 return existing
#         else:
#             new_product = Product(
#                 nombre=product.nombre,
#                 descripcion=product.descripcion,
#                 precio_unitario=product.precio_unitario,
#                 stock=product.stock
#             )
#             self.db.add(new_product)
#             self.db.commit()
#             self.db.refresh(new_product)
#             return new_product

#     def delete(self, product_id: int):
#         product = self.get_by_id(product_id)
#         if product:
#             self.db.delete(product)
#             self.db.commit()
#             return True
#         return False

from app.domain.models.products import Product
from sqlalchemy.orm import Session
from datetime import datetime

class SQLProductRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self):
        return self.db.query(Product).all()

    def get_by_id(self, product_id: int):
        return self.db.query(Product).filter_by(producto_id=product_id).first()


    def save(self, product: Product):
        try:
            if product.producto_id:
                # Update existing product
                existing = self.get_by_id(product.producto_id)
                if existing:
                    existing.nombre = product.nombre
                    existing.descripcion = product.descripcion
                    existing.precio_unitario = product.precio_unitario
                    existing.stock = product.stock
                    # Ensure 'estado' is updated if provided, but 'fecha_creacion' should not be changed
                    existing.estado = product.estado if product.estado else existing.estado
                    self.db.commit()  # Commit only after all changes are done
                    self.db.refresh(existing)  # Refresh the object with the latest data
                    return existing
                else:
                    raise ValueError(f"Product with ID {product.producto_id} does not exist.")
            else:
                # Create a new product
                new_product = Product(
                    nombre=product.nombre,
                    descripcion=product.descripcion,
                    precio_unitario=product.precio_unitario,
                    stock=product.stock,
                    estado=product.estado or 'A',  # Default to 'A' if estado is not provided
                    fecha_creacion=product.fecha_creacion or datetime.utcnow()  # Set current time if not provided
                )
                self.db.add(new_product)
                self.db.commit()  # Commit to save the new product
                self.db.refresh(new_product)  # Refresh to get the product with the database-generated fields
                return new_product

        except Exception as e:
            # Rollback in case of any error
            self.db.rollback()
            raise e  # Re-raise the exception to handle it at a higher level
        

    # def save(self, product: Product):
    #     if product.producto_id:
    #         existing = self.get_by_id(product.producto_id)
    #         if existing:
    #             # Update existing product
    #             existing.nombre = product.nombre
    #             existing.descripcion = product.descripcion
    #             existing.precio_unitario = product.precio_unitario
    #             existing.stock = product.stock
    #             # Ensure estado and fecha_creacion are updated if needed
    #             existing.estado = product.estado if product.estado else existing.estado
    #             existing.fecha_creacion = product.fecha_creacion if product.fecha_creacion else existing.fecha_creacion
    #             self.db.commit()
    #             self.db.refresh(existing)
    #             return existing
    #     else:
    #         # Create a new product
    #         new_product = Product(
    #             nombre=product.nombre,
    #             descripcion=product.descripcion,
    #             precio_unitario=product.precio_unitario,
    #             stock=product.stock,
    #             estado=product.estado or 'A',  # Default to 'A' for Active
    #             fecha_creacion=product.fecha_creacion or datetime.utcnow()  # Set current timestamp by default
    #         )
    #         self.db.add(new_product)
    #         self.db.commit()
    #         self.db.refresh(new_product)
    #         return new_product

    def delete(self, product_id: int):
        product = self.get_by_id(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()
            return True
        return False
