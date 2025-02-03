from app.models.user import User
from app import db

def register_user(username, password):
    # Kiểm tra xem username đã tồn tại chưa
    if User.query.filter_by(username=username).first():
        return None  # Username đã tồn tại

    # Tạo user mới
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user  # Đăng nhập thành công
    return None  # Sai username hoặc password