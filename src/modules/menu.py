"""MAIN"""
import sys
from PySide6.QtWidgets import QMainWindow, QStackedWidget
from view.menu import Ui_menuWindow
from modules.user import UsersWindow


class MenuWindow(QMainWindow,Ui_menuWindow):
    def __init__(self, logedUser):
        super().__init__()
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.setupUi(self)
        self.handlerMenu()

    def handlerMenu(self):
        self.setUser()
        self.connection()

    def setUser(self):
        if self.user[6] != "ADMINISTRADOR":
            self.btn_users.hide()
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[2]}")

    def connection(self):
        self.btn_users.clicked.connect(self.users_menu)
        # self.btn_clients.clicked.connect()
        # self.btn_account.clicked.connect()
        # self.btn_transactions.clicked.connect()
        # self.btn_logout.clicked.connect()
    
    def users_menu(self):
        self.close()
        self.users = UsersWindow(self.logedUser, self)
        self.users.show()  


    


