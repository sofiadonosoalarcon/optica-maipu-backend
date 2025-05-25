from app.domain.models.products import Product
from app.infraestructure.utils.exceptions import ProductCreationError

class ProductUseCases:
    def __init__(self, product_repo):
        self.product_repo = product_repo

    def list_products(self):
        return self.product_repo.get_all()

    def get_product(self, product_id):
        return self.product_repo.get_by_id(product_id)

    def create_product(self, data):
        try:
            data.pop("id", None)  # Elimina id si viene en el payload
            product = Product(**data)
            product = self.product_repo.save(product)
            if not product:
                raise ProductCreationError("Failed to create product")
            return product
        except Exception as e:
            raise ProductCreationError(f"Error creating product: {e}") from e



    def update_product(self, product_id, data):
        product = self.product_repo.get_by_id(product_id)
        if product:
            product.name = data.get("name", product.name)
            product.price = data.get("price", product.price)
            product.stock = data.get("stock", product.stock)
            self.product_repo.save(product)
        return product

    def delete_product(self, product_id):
        return self.product_repo.delete(product_id)
