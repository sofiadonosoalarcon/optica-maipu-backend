"""from flask import Flask
from adapters.input.flask_app.routes import register_routes

def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)"""

from flask import Flask
from adapters.input.flask_app.routes import register_routes

def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app

app = create_app()  # 👈 Esto es necesario para gunicorn

if __name__ == '__main__':
    app.run(debug=True)
