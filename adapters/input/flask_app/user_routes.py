
from flask_restx import Namespace, Resource, fields
from adapters.output.repositories.user_repository import UserRepository
from app.domain.use_cases.services.user_service import UserService

# Crear namespace
ns_users = Namespace('Usuarios', description='Operaciones relacionadas con usuarios')

# Inyección de dependencias
user_repository = UserRepository()
user_service = UserService(user_repository)

# Modelo para documentación Swagger
user_model = ns_users.model('User', {
    'id': fields.Integer(readonly=True),
    'nombre': fields.String,
    'email': fields.String
})

@ns_users.route('/<int:user_id>')
@ns_users.param('user_id', 'ID del usuario')
class UserResource(Resource):
    @ns_users.response(200, 'Usuario encontrado', user_model)
    @ns_users.response(404, 'Usuario no encontrado')
    def get(self, user_id):
        user = user_service.get_user(user_id)
        if user:
            return vars(user), 200
        return {'message': 'Usuario no encontrado'}, 404

__all__ = ['ns_users']