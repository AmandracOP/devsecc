from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main import Ui_MainWindow
import sys

class AgentApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Connect signals and slots here if needed

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AgentApp()
    window.show()
    sys.exit(app.exec_())
