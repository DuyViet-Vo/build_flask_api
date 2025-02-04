# Flask API Project

Đây là một dự án Backend API được xây dựng bằng Flask. Dự án bao gồm các tính năng cơ bản như đăng ký, đăng nhập, và các endpoint API khác.

## Hướng dẫn chạy code

### 1. Cài đặt môi trường

Đảm bảo bạn đã cài đặt Python 3.x và pip. Sau đó, tạo một môi trường ảo và kích hoạt nó:

```
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
```
### 2. Cài đặt các dependencies
Cài đặt các dependencies cần thiết bằng cách chạy lệnh sau:
```
pip install -r requirements.txt
```
### 3. Cấu hình biến môi trường
Tạo một file .env trong thư mục gốc của dự án và thêm các biến môi trường sau:
```
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///app.db
JWT_SECRET_KEY=your_jwt_secret_key
```
### 4. Khởi tạo database
Chạy các lệnh sau để khởi tạo và áp dụng các migration:
```
flask db init
flask db migrate
flask db upgrade
```
### 5. Chạy ứng dụng
Chạy ứng dụng bằng lệnh:
```
python run.py
```
## Các file quan trọng
app/__init__.py
Khởi tạo Flask app và các extensions.

Load cấu hình từ config.py.

Đăng ký các blueprint thông qua hàm register_blueprints.

app/extensions.py
Quản lý các extensions như db, migrate, và jwt.

Giúp tránh lỗi circular import bằng cách tách biệt các extensions.

app/register_blueprints.py
Đăng ký tất cả các blueprint với Flask app.

Giúp quản lý các route một cách có tổ chức.

app/models/user.py
Định nghĩa model User cho database.

Bao gồm các trường như id, username, và password.

app/routes/auth.py
Chứa các endpoint liên quan đến xác thực như đăng ký và đăng nhập.

Sử dụng các service từ app/services/auth_service.py để xử lý logic.

app/services/auth_service.py
Chứa các hàm xử lý logic nghiệp vụ như đăng ký và đăng nhập.

Tương tác với model User để thao tác với database.

app/config.py
Load các biến môi trường từ file .env.

Cung cấp cấu hình cho Flask app.

run.py
File chính để chạy ứng dụng.

Gọi hàm create_app từ app/__init__.py để khởi tạo và chạy ứng dụng.
## Testing
Để chạy các test case, sử dụng lệnh sau:
```python -m unittest discover tests```