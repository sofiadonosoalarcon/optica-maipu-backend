import os
from dotenv import load_dotenv


class BaseConfig:
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv("SECRET_KEY") 


class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True

config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
