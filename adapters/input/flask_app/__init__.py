# adapters/input/flask_app/__init__.py

from flask import Flask
# from .routes import bp  ←❌ Eliminado porque bp ya no se usa

def create_app():
    app = Flask(__name__)
    return app
