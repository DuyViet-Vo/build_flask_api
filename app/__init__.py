from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, migrate, jwt
from .register_blueprints import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources=Config.CORS_RESOURCES)

    # Khởi tạo các extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Đăng ký các blueprint
    register_blueprints(app)

    return app
