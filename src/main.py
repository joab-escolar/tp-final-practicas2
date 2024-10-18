"""MAIN"""
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from view.login import Ui_LoginWindow
from database.migrations import DataBase

class LoginWindow(QMainWindow,Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.handler()
        
    def handler(self):
        self.startDB()

    def startDB(self):
        db = DataBase()
        db.migrate()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
