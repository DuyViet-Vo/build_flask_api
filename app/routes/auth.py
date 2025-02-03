from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.services.auth_service import register_user, login_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = register_user(username, password)
    if not user:
        return jsonify({"message": "Username already exists"}), 400

    return (
        jsonify(
            {
                "message": "User registered successfully",
                "user": {"id": user.id, "username": user.username},
            }
        ),
        201,
    )


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = login_user(username, password)
    if not user:
        return jsonify({"message": "Invalid username or password"}), 401

    # Tạo JWT token
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200
