"""MAIN"""
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from database.migrations import DataBase
from view.login import Ui_LoginWindow
from modules.login import Login
from modules.menu import MenuWindow

class LoginWindow(QMainWindow,Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.handlerLogin()

    def handlerLogin(self):
        self.startDB()
        self.connection()

    def startDB(self):
        db = DataBase()
        db.migrate()

    def connection(self):
        self.btn_ingresar.clicked.connect(self.login)

    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        #debug
        username = 'admin'
        password = 'admin'

        login = Login()
        logedUser = login.login(username, password)
        print(logedUser)

        self.lbl_error.setText("")

        if logedUser != False:
            self.close()
            self.menu = MenuWindow(logedUser)
            self.menu.show()
        else:
            self.lbl_error.setText("credenciales incorrectas!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
