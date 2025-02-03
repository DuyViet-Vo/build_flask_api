from flask import Blueprint
from .auth import auth_bp  # Giả sử bạn đã định nghĩa auth_bp trong file auth.py

def init_app(app):
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
