import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main_ui import Ui_MainWindow
from login import LoginWindow
from registration import RegistrationWindow

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Initialize components here

    def show_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()

    def show_registration(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
