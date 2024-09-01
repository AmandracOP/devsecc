from PyQt5.QtWidgets import QDialog
from ui.register_ui import Ui_RegisterWindow
import requests

class RegistrationWindow(QDialog, Ui_RegisterWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_button.clicked.connect(self.handle_registration)

    def handle_registration(self):
        username = self.username_input.text()
        password = self.password_input.text()
        response = requests.post("http://localhost:5000/register", json={"username": username, "password": password})
        if response.status_code == 201:
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Registration failed!")
