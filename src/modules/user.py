"""MAIN"""
import sys
from PySide6.QtWidgets import QMainWindow
from view.user import Ui_usersWindow
from view.user_create import Ui_usersCreateWindow
from utils.sqlRaw import sql
from database.UsersDB import UsersDB

# MAIN USER WINDOWS 
class UsersWindow(QMainWindow,Ui_usersWindow):
    def __init__(self, logedUser, fatherInstance):
        super().__init__()
        self.fatherInstance = fatherInstance
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.setupUi(self)
        self.handlerUsers()
    
    def handlerUsers(self):
        self.setUser()
        self.showList()
        self.connection()

    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[2]}")

    def showList(self):
        self.list_users.clear()
        users = sql("SELECT * FROM users;")
        for item in users:
            user = list(item)
            role =  list(sql(f"SELECT * FROM roles WHERE id = {user[3]}")[0])
            self.list_users.addItem(f"ID:   {user[0]}   USUARIO:{user[1]}   ROL:{role[1]}   ULTIMA CON:{user[5]}")

    def connection(self):
        self.btn_back.clicked.connect(self.goBack)
        self.btn_create.clicked.connect(self.showCreate)

    def goBack(self):
        self.close()
        self.fatherInstance.show()

    def showCreate(self):
        self.close()
        self.userCreate = UsersCreateWindow(self.logedUser, self)
        self.userCreate.show()

# CREATE USER WINDOW
class UsersCreateWindow(QMainWindow,Ui_usersCreateWindow):
    def __init__(self, logedUser, fatherInstance):
        super().__init__()
        self.fatherInstance = fatherInstance
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.setupUi(self)
        self.handlerUsers()

    def handlerUsers(self):
        self.setUser()
        self.mapRoles()
        self.connection()
        
    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[2]}")

    def mapRoles(self):
        roles = sql("SELECT * FROM roles;")
        for id, role in roles:
            self.slect_roles.addItem(role)
            self.slect_roles.setItemData(self.slect_roles.count() - 1,id)
            
    def connection(self):
        self.btn_back.clicked.connect(self.goBack)
        self.btn_store.clicked.connect(self.store)

    def goBack(self):
        self.close()
        self.fatherInstance.show()

    def store(self):
        username = str(self.input_username.text())
        password = str(self.input_password.text())
        role = self.slect_roles.currentIndex()
        role_id = self.slect_roles.itemData(role)

        newUser = UsersDB().store(username, password, role_id)

        self.fatherInstance.showList()
        self.goBack()




        