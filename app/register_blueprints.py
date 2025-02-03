from .routes.auth import auth_bp


def register_blueprints(app):
    """
    Đăng ký tất cả các blueprint với Flask app.
    """
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
