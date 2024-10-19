"""MAIN"""
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from view.login import Ui_LoginWindow
from database.migrations import DataBase
from modules.login import Login

class LoginWindow(QMainWindow,Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.handler()

    def connection(self):
        self.btn_ingresar.clicked.connect(self.login)

    def handler(self):
        self.startDB()
        self.connection()

    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        login = Login()
        login.login(username, password)

    def startDB(self):
        db = DataBase()
        db.migrate()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
