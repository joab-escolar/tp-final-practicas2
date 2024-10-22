"""MAIN"""
import sys
from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox
from view.user import Ui_usersWindow
from view.user_create import Ui_usersIterableWindow
# from view.users import Ui_usersIterateWindow
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
        self.loadTable()
        self.showTable()
        self.connection()

    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[2]}")

    def loadTable(self):
        self.table_user.setColumnCount(4)
        self.table_user.setHorizontalHeaderLabels(["ID" ,"usuario", "rol", "ultam coneccion", "creacion"])
        self.table_user.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table_user.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

    def showTable(self):
        self.table_user.setRowCount(0)
        users = sql("SELECT * FROM users;")
        for item in users:
            user = list(item)
            role =  list(sql(f"SELECT * FROM roles WHERE id = {user[3]}")[0])
            row_position = self.table_user.rowCount()
            self.table_user.insertRow(row_position)
            self.table_user.setItem(row_position, 0, QTableWidgetItem(f"{user[0]}"))
            self.table_user.setItem(row_position, 1, QTableWidgetItem(user[1]))
            self.table_user.setItem(row_position, 2, QTableWidgetItem(role[1]))
            self.table_user.setItem(row_position, 3, QTableWidgetItem(user[4]))


    def connection(self):
        self.btn_back.clicked.connect(self.goBack)
        self.btn_create.clicked.connect(self.showCreate)
        self.btn_edit.clicked.connect(self.showEdit)
        self.btn_delete.clicked.connect(self.delete)

    def goBack(self):
        self.close()
        self.fatherInstance.show()

    def showCreate(self):
        self.close()
        self.userCreate = UsersCreateWindow(self.logedUser, self)
        self.userCreate.show()

    def showEdit(self):
        selectedRow = self.table_user.currentRow()
        if selectedRow >= 0:
            self.close()
            self.userEdit = UsersEditWindow(self.logedUser, self, self.table_user.item(selectedRow,0).text())
            self.userEdit.show()
        else:
            print("error")

    def delete(self):
        selectedRow = self.table_user.currentRow()
        userID = int(self.table_user.item(selectedRow,0).text())
        UsersDB().delete(userID)
        self.showTable()

# CREATE USER WINDOW
class UsersCreateWindow(QMainWindow,Ui_usersIterableWindow):
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
        username = str(self.input_username.text()).strip()
        password = str(self.input_password.text()).strip()
        role = self.slect_roles.currentIndex()
        role_id = self.slect_roles.itemData(role)
    
        if not username:
            QMessageBox.warning(self, "Error", "El campo de nombre de usuario está vacío.")
            return

        if not password:
                QMessageBox.warning(self, "Error", "El campo de contraseña está vacío.")
                return
    
        if role == -1:
                QMessageBox.warning(self, "Error", "No se ha seleccionado ningún rol.")
                return

        newUser = UsersDB().store(username, password, role_id)

        self.fatherInstance.showTable()
        self.goBack()

class UsersEditWindow(QMainWindow,Ui_usersIterableWindow):
    def __init__(self, logedUser, fatherInstance, userID):
        super().__init__()
        self.fatherInstance = fatherInstance
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.udateUserID = int(userID)
        self.setupUi(self)
        self.handlerUsers()

    def handlerUsers(self):
        self.setUser()
        self.mapRoles()
        self.loadValues()
        self.connection()
        
    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[2]}")

    def mapRoles(self):
        roles = sql("SELECT * FROM roles;")
        for id, role in roles:
            self.slect_roles.addItem(role)
            self.slect_roles.setItemData(self.slect_roles.count() - 1,id)
    
    def loadValues(self):
        updateUser = list(sql(f"SELECT * FROM users WHERE id = {self.udateUserID};")[0])
        self.input_username.setText(updateUser[1])
        for index in range(self.slect_roles.count()):
            if self.slect_roles.itemData(index) == updateUser[3]:
                self.slect_roles.setCurrentIndex(index)
                break

    def connection(self):
        self.btn_back.clicked.connect(self.goBack)
        self.btn_store.clicked.connect(self.update)

    def goBack(self):
        self.close()
        self.fatherInstance.show()

    def update(self):
        username = str(self.input_username.text())
        password = str(self.input_password.text())
        role = self.slect_roles.currentIndex()
        role_id = self.slect_roles.itemData(role)
    
        if not username:
            QMessageBox.warning(self, "Error, Nombre vacio.")
            return 
        
        UsersDB().update(username, password, role_id, self.udateUserID)

        self.fatherInstance.showTable()
        self.goBack()


        