from PyQt5.QtWidgets import QDialog
from ui.login_ui import Ui_LoginWindow
from PyQt5.QtWidgets import QMessageBox
import requests

class LoginWindow(QDialog, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        response = requests.post("http://localhost:5000/login", json={"username": username, "password": password})
        if response.status_code == 200:
            QMessageBox.information(self, "Success", "Login successful!")
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials!")
