import json
import os

AUTH_FILE = "auth.json"


def load_users():
    if not os.path.exists(AUTH_FILE):
        return {}

    with open(AUTH_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):
    with open(AUTH_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)


def register_user(email, password):
    # ❌ Thiếu thông tin
    if not email or not password:
        return False, "Vui lòng nhập đầy đủ email và mật khẩu"

    users = load_users()

    # ❌ Email đã tồn tại
    if email in users:
        return False, "Email đã tồn tại"

    # ✅ Tạo tài khoản
    users[email] = password
    save_users(users)

    return True, "Đăng ký thành công"


def check_login(email, password):
    users = load_users()

    if not email or not password:
        return False, "Vui lòng nhập đầy đủ thông tin"

    if email not in users:
        return False, "Email không tồn tại"

    if users[email] != password:
        return False, "Sai mật khẩu"

    return True, "Login successful"