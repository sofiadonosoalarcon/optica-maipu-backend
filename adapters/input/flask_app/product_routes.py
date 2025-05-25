from flask_restx import Namespace, Resource, fields, reqparse
from adapters.output.repositories.product_repo_memory import InMemoryProductRepository
from app.domain.use_cases.product_use_cases import ProductUseCases

# Crear namespace para productos
ns_products = Namespace('Productos', description='Operaciones relacionadas con productos')

# Inyección de dependencias
product_repo = InMemoryProductRepository()
product_use_cases = ProductUseCases(product_repo)

# Modelo para documentación Swagger
product_model = ns_products.model('Product', {
    'id': fields.Integer(readonly=True),
    'nombre': fields.String(required=True, description='Nombre del producto'),
    'descripcion': fields.String(required=True, description='Descripción del producto'),
    'precio_unitario': fields.Float(required=True, description='Precio unitario del producto'),
    'stock': fields.Integer(description='Stock disponible')
})

# Parser para entrada POST/PUT
product_parser = ns_products.parser()
product_parser.add_argument('id', type=int, required=True, help='ID del producto', location='json')
product_parser.add_argument('nombre', type=str, required=True, help='Nombre del producto', location='json')
product_parser.add_argument('descripcion', type=str, required=True, help='Descripción del producto', location='json')
product_parser.add_argument('precio_unitario', type=float, required=True, help='Precio unitario del producto', location='json')
product_parser.add_argument('stock', type=int, help='Stock disponible', location='json')

# Definición de rutas y métodos
# Ruta base para productos
@ns_products.route('/')
class ProductList(Resource):
    @ns_products.marshal_list_with(product_model)
    def get(self):
        """Listar todos los productos"""
        products = product_use_cases.list_products()
        return products

    @ns_products.expect(product_parser)
    @ns_products.marshal_with(product_model, code=201)
    def post(self):
        """Crear un nuevo producto"""
        args = product_parser.parse_args()
        product = product_use_cases.create_product(args)
        return product, 201

# Ruta para un producto específico
@ns_products.route('/<int:product_id>')
@ns_products.param('product_id', 'ID del producto')
class ProductResource(Resource):
    @ns_products.marshal_with(product_model)
    def get(self, product_id):
        """Obtener un producto por ID"""
        product = product_use_cases.get_product(product_id)
        if product:
            return product
        ns_products.abort(404, "Producto no encontrado")

    @ns_products.expect(product_parser)
    @ns_products.marshal_with(product_model)
    def put(self, product_id):
        """Actualizar un producto existente"""
        args = product_parser.parse_args()
        product = product_use_cases.update_product(product_id, args)
        if product:
            return product
        ns_products.abort(404, "Producto no encontrado")

    @ns_products.response(204, 'Producto eliminado')
    @ns_products.doc('delete_product')
    def delete(self, product_id):
        """Eliminar un producto"""
        result = product_use_cases.delete_product(product_id)
        if result:
            return {'message': 'Producto eliminado'}, 200
        ns_products.abort(404, "Producto no encontrado")

__all__ = ['ns_products']
