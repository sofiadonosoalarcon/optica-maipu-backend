from app.domain.models.products import Product

class InMemoryProductRepository:
    def __init__(self):
        self.products = {}
        self.counter = 1

    def get_all(self):
        return list(self.products.values())

    def get_by_id(self, product_id):
        return self.products.get(product_id)

    def save(self, product: Product):
        if product.id is None:
            product.id = self.counter
            self.counter += 1
        self.products[product.id] = product

    def delete(self, product_id):
        return self.products.pop(product_id, None)
