import sys
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGraphicsDropShadowEffect, QLineEdit
)
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt
from auth import check_login


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        # ================== LOAD UI ==================
        uic.loadUi("UI/buoi8.ui", self)

        # ================== WINDOW SETUP ==================
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background: transparent;")

        # ================== INPUT SETUP ==================
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)

        # ================== CONNECT SIGNALS ==================
        self.btnExit.clicked.connect(self.close)
        self.btnMinimize.clicked.connect(self.showMinimized)
        self.btnLogin.clicked.connect(self.handle_login)
        self.btnRegister.clicked.connect(self.open_register)

        self.checkShowPassword.stateChanged.connect(self.toggle_password)

        self.lineEditEmail.textChanged.connect(self.hide_error)
        self.lineEditPassword.textChanged.connect(self.hide_error)

        # ================== STYLE & EFFECT ==================
        self.setup_main_style()
        self.setup_shadow()
        self.setup_logo_shadow()
        self.setup_btnExit()
        self.setup_btnMinimize()
        self.setup_checkbox()

        # ================== ERROR LABEL ==================
        self.labelError.hide()

    # =====================================================
    # ================== STYLE METHODS ====================
    # =====================================================

    def setup_main_style(self):
        self.widget.setStyleSheet("""
        #widget {
            background-color: rgba(30,30,30,220);
            border-radius: 28px;
            border: 1px solid rgba(255,255,255,30);
        }

        QLabel {
            background: transparent;
            color: white;
            font-size: 14px;
            font-family: 'Segoe UI';
        }

        QLineEdit {
            background-color: rgba(60,60,60,180);
            color: white;
            border-radius: 10px;
            padding: 8px;
            border: 1px solid rgba(255,255,255,50);
        }
        """)

        self.labelError.setStyleSheet("""
        QLabel {
            color: #ff5f57;
            font-size: 12px;
        }
        """)

    def setup_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(40)
        shadow.setOffset(0, 10)
        shadow.setColor(QColor(0, 0, 0, 150))
        self.widget.setGraphicsEffect(shadow)

    def setup_logo_shadow(self):
        # labelLogo PHẢI là objectName của logo trong Designer
        if hasattr(self, "labelLogo"):
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(30)
            shadow.setOffset(0, 6)
            shadow.setColor(QColor(0, 0, 0, 160))
            self.labelLogo.setGraphicsEffect(shadow)

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

    def setup_checkbox(self):
        self.checkShowPassword.setStyleSheet("""
        QCheckBox {
            color: white;
            font-size: 13px;
            spacing: 6px;
        }
        """)

    # =====================================================
    # ================== LOGIC METHODS ====================
    # =====================================================

    def toggle_password(self, state):
        if state == Qt.CheckState.Checked.value:
            self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)

    def hide_error(self):
        self.labelError.hide()

    def open_register(self):
        from Register import RegisterWindow
        self.register_window = RegisterWindow(self)  # truyền self
        self.register_window.show()
        self.hide()

    def handle_login(self):
        email = self.lineEditEmail.text().strip()
        password = self.lineEditPassword.text().strip()

        success, message = check_login(email, password)

        if success:
            print("Login success")
        else:
            self.labelError.setText(message)
            self.labelError.show()


# ================== RUN APP ==================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
