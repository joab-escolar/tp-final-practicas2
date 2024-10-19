"""MAIN"""
import sys
from PySide6.QtWidgets import QMainWindow
from view.user import Ui_usersWindow
from utils.sqlRaw import sql


class UsersWindow(QMainWindow,Ui_usersWindow):
    def __init__(self, logedUser):
        super().__init__()
        self.user = logedUser
        self.setupUi(self)
    
    def handlerMenu(self):
        self.setUser()

    # def connection(self):
        

    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[2]}")