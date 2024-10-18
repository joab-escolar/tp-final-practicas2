"""MAIN"""
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from view.login import Ui_LoginWindow as LoginWindow

class Banco(QMainWindow,LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Banco()
    window.show()
    sys.exit(app.exec_())
