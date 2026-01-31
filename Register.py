import sys
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QGraphicsDropShadowEffect, QLineEdit
)
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt
from auth import register_user


class RegisterWindow(QWidget):
    def __init__(self, login_window=None):
        super().__init__()
        self.login_window = login_window  # giữ tham chiếu Login

        # ===== LOAD UI =====
        uic.loadUi("UI/register.ui", self)

        # ===== WINDOW SETUP =====
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background: transparent;")
        self.setup_checkbox()

        # ===== INPUT SETUP =====
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)

        # ===== CONNECT SIGNALS =====
        self.btnExit.clicked.connect(self.close)
        self.btnMinimize.clicked.connect(self.showMinimized)
        self.btnBack.clicked.connect(self.back_to_login)
        self.checkShowPassword.stateChanged.connect(self.toggle_password)
        self.btnRegister.clicked.connect(self.handle_register)

        # ===== ERROR LABEL =====
        self.labelError.hide()
        self.labelError.setStyleSheet("""
            QLabel {
                color: #ff5f57;
                font-size: 12px;
            }
        """)

        # ===== STYLE =====
        self.setup_main_style()
        self.setup_shadow()
        self.setup_btnExit()
        self.setup_btnMinimize()

    # ================= STYLE =================

    def setup_main_style(self):
        self.widget.setStyleSheet("""
            #widget {
                background-color: rgba(30, 30, 30, 230);
                border-radius: 28px;
                border: 1px solid rgba(255,255,255,30);
            }

            QLabel {
                background: transparent;
                color: white;
                font-family: 'Segoe UI';
                font-size: 14px;
            }

            QLineEdit {
                background-color: rgba(60,60,60,180);
                color: white;
                border-radius: 10px;
                padding: 8px;
                border: 1px solid rgba(255,255,255,50);
            }
        """)

    def setup_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(40)
        shadow.setOffset(0, 10)
        shadow.setColor(QColor(0, 0, 0, 150))
        self.widget.setGraphicsEffect(shadow)

    def setup_btnExit(self):
        self.btnExit.setStyleSheet("""
            QPushButton {
                background-color: #ff5f57;
                border-radius: 6px;
                border: none;
                color: transparent;
                font-size: 9px;
                font-weight: bold;
            }
            QPushButton:hover {
                color: #7a0c0c;
            }
        """)

    def setup_btnMinimize(self):
        self.btnMinimize.setStyleSheet("""
            QPushButton {
                background-color: #ffbd2e;
                border-radius: 6px;
                border: none;
                color: transparent;
                font-size: 9px;
                font-weight: bold;
            }
            QPushButton:hover {
                color: #7a4a00;
            }
        """)

    # ================= LOGIC =================

    def toggle_password(self, state):
        if state == Qt.CheckState.Checked.value:
            self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)

    def handle_register(self):
        email = self.lineEditEmail.text().strip()
        password = self.lineEditPassword.text().strip()

        if not email or not password:
            self.labelError.setText("Vui lòng nhập đầy đủ thông tin")
            self.labelError.show()
            return

        # Demo – chưa lưu DB
        self.labelError.setStyleSheet("color: #4cd964;")
        self.labelError.setText("Tạo tài khoản thành công")
        self.labelError.show()

    def back_to_login(self):
        if self.login_window is not None:
            self.login_window.show()
        self.close()


    def setup_checkbox(self):
        self.checkShowPassword.setStyleSheet("""
        QCheckBox {
            color: white;
            font-size: 13px;
            spacing: 6px;
        }
        """)

    def handle_register(self):
        email = self.lineEditEmail.text().strip()
        password = self.lineEditPassword.text().strip()

        success, message = register_user(email, password)

        if success:
            self.labelError.setStyleSheet("color: #2ecc71;")
            self.labelError.setText(message)
            self.labelError.show()

        # quay về login sau 1 chút
            self.close()
            self.login_window.show()
        else:
            self.labelError.setStyleSheet("color: #ff5f57;")
            self.labelError.setText(message)
            self.labelError.show()

    def back_to_login(self):
        self.login_window.show()
        self.close()

        


# ===== CHẠY RIÊNG REGISTER (TEST) =====
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = RegisterWindow()
    w.show()
    sys.exit(app.exec())
