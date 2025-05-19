from flask import Blueprint
from adapters.input.flask_app.controllers.user_controller import get_user_controller
from app.use_cases.user_service import UserService
from adapters.output.repositories.user_repository import UserRepository

bp = Blueprint('routes', __name__)

# Inyección de dependencias manual
user_repository = UserRepository()
user_service = UserService(user_repository)

bp.add_url_rule('/users/<user_id>', 'get_user', get_user_controller(user_service))
