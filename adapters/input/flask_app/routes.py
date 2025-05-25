from flask import Blueprint
from flask_restx import Api
from .user_routes import ns_users
from .product_routes import ns_products  # Ajusta según tu estructura

bp = Blueprint('routes', __name__)

api = Api(
    bp,
    version='1.0.0',
    openapi='3.0.0',
    title='Óptica Maipú API',
    description='API para la gestión de usuarios y productos en el sistema de Óptica Maipú.',
    default='General',
    default_label='Operaciones Generales',
    validate=True,
    swagger_ui_config={
        'docExpansion': 'list',
        'defaultModelsExpandDepth': -1,
        'filter': True,
        'displayRequestDuration': True,
        'deepLinking': True,
        'persistAuthorization': True
    }
)

api.add_namespace(ns_users, path='/users')
api.add_namespace(ns_products, path='/products')

def register_routes(app):
    app.register_blueprint(bp)
