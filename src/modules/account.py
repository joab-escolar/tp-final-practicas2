"""MAIN"""
import sys
from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox
from PySide6.QtCore import QDateTime 
from view.cuentas import Ui_cuentasWindow
from view.cuenta_create import Ui_CuentasIterableWindow
from view.cuentas_info import Ui_cuentasInfoWindow
from utils.sqlRaw import sql, sqlCount
from database.accountsDB import AccountsDB

# MAIN USER WINDOWS 
class AccountWindow(QMainWindow,Ui_cuentasWindow):
    def __init__(self, logedUser, fatherInstance):
        super().__init__()
        self.fatherInstance = fatherInstance
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.setupUi(self)
        self.handlerCuentas()
    
    def handlerCuentas(self):
        self.setUser()
        self.loadTable()
        self.showTable()
        self.connection()

    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[2]}")

    def loadTable(self):
        self.table_accounts.setColumnCount(8)
        self.table_accounts.setHorizontalHeaderLabels(["ID" ,"cbu", "titular", "tipo", "alias", "Balance", "Creacion", "Estado"])
        self.table_accounts.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table_accounts.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

    def showTable(self):
        self.showStatistics()
        self.table_accounts.setRowCount(0)
        accounts = sql("SELECT * FROM accounts WHERE status = 1;")
        for item in accounts:
            account = list(item)
            client =  list(sql(f"SELECT * FROM clients WHERE id = {account[2]}")[0])
            row_position = self.table_accounts.rowCount()
            self.table_accounts.insertRow(row_position)
            self.table_accounts.setItem(row_position, 0, QTableWidgetItem(f"{account[0]}"))
            self.table_accounts.setItem(row_position, 1, QTableWidgetItem(f"{account[1]}"))
            self.table_accounts.setItem(row_position, 2, QTableWidgetItem(f"{client[2]} {client[1]}"))
            self.table_accounts.setItem(row_position, 3, QTableWidgetItem(account[3]))
            self.table_accounts.setItem(row_position, 4, QTableWidgetItem(account[4]))
            self.table_accounts.setItem(row_position, 5, QTableWidgetItem(f"{account[5]}"))
            self.table_accounts.setItem(row_position, 6, QTableWidgetItem(account[6]))
            self.table_accounts.setItem(row_position, 7, QTableWidgetItem(f"{account[7]}"))

    def showStatistics(self):
        total_accounts = sqlCount("SELECT COUNT(*) FROM accounts WHERE status = 1;")[0]
        total_positive_accounts = sqlCount("SELECT COUNT(*) FROM accounts WHERE balance >= 0 AND status = 1;")[0]
        top_accounts = AccountsDB().getTopAccounts()
        self.lbl_total_accounts.setText(f"TOTAL CUENTAS: {total_accounts}")
        self.lbl_total_positive_accounts.setText(f"CUENTAS POSITIVAS: {total_positive_accounts}")
        self.list_estadistica.clear()
        for item in top_accounts:
            self.list_estadistica.addItem(f"ALIAS: {item[1]}, CANT: {item[2]}")

    def connection(self):
        self.btn_back.clicked.connect(self.goBack)
        self.btn_create.clicked.connect(self.showCreate)
        self.btn_edit.clicked.connect(self.showEdit)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_history.clicked.connect(self.history)

    def goBack(self):
        self.close()
        self.fatherInstance.show()

    def showCreate(self):
        self.close()
        self.clientCreate = AccountCreateWindow(self.logedUser, self)
        self.clientCreate.show()

    def showEdit(self):
        selectedRow = self.table_accounts.currentRow()
        if selectedRow >= 0:
            self.close()
            self.accountEdit = AccountEditWindow(self.logedUser, self, self.table_accounts.item(selectedRow,0).text())
            self.accountEdit.show()
        else:
            QMessageBox.warning(self, "Error", "Seleccione una fila!!")
            return

    def delete(self):
        selectedRow = self.table_accounts.currentRow()
        if selectedRow >= 0:
            deletedID = int(self.table_accounts.item(selectedRow,0).text())
            AccountsDB().delete(deletedID)
            self.showTable()
        else:
            QMessageBox.warning(self, "Error", "Seleccione una fila!!")
            return
       

    def history(self):
        selectedRow = self.table_accounts.currentRow()
        if selectedRow >= 0:
            self.close()
            self.accountEdit = HistoryWindow(self.logedUser, self, self.table_accounts.item(selectedRow,0).text())
            self.accountEdit.show()
        else:
            QMessageBox.warning(self, "Error", "Seleccione una fila!!")
            return

# CREATE USER WINDOW
class AccountCreateWindow(QMainWindow,Ui_CuentasIterableWindow):
    def __init__(self, logedUser, fatherInstance):
        super().__init__()
        self.fatherInstance = fatherInstance
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.setupUi(self)
        self.handlerCuentas()

    def handlerCuentas(self):
        self.setUser()
        self.uploadValues()
        self.connection()
        
    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[2]}")

    def connection(self):
        self.btn_back.clicked.connect(self.goBack)
        self.btn_crear.clicked.connect(self.store)

    def goBack(self):
        self.close()
        self.fatherInstance.show()

    def uploadValues(self):
        clients = sql("SELECT * FROM clients;")
        for item in clients:
            listItem = list(item)
            self.slect_titular.addItem(f"{listItem[2]} {listItem[1]}")
            self.slect_titular.setItemData(self.slect_titular.count() - 1, listItem[0])

    def store(self):
        cbu = self.input_cbu.text()
        type = self.input_tipo.text()
        alias = self.input_alias.text()
        balance = self.input_balance.text()
        client = self.slect_titular.currentIndex()
        client_id = self.slect_titular.itemData(client)
        
        if not cbu:
            QMessageBox.warning(self, "Error", "Rellene el campo CBU")
            return
        if not cbu.isdigit():
            QMessageBox.warning(self, "Error", "El cbu debe ser numerico")
            return
        if len(sql(f"SELECT * FROM accounts WHERE cbu = '{cbu}';")) != 0:
            QMessageBox.warning(self, "Error", "El cbu ya existe!!")
            return

        if not type:
            QMessageBox.warning(self, "Error", "Elija un tipo")
            return
        
        if not alias:
            QMessageBox.warning(self, "Error", "Porfavor Rellene el Alias")
            return
        if len(sql(f"SELECT * FROM accounts WHERE alias = '{alias}';")) != 0:
            QMessageBox.warning(self, "Error", "El alias ya existe!!")
            return

        if not balance:
            QMessageBox.warning(self, "Error", "Rellene el campo Balance inicial")
            return
        if not balance.isdigit():
            QMessageBox.warning(self, "Error", "Porvavor ingrese solo datos numericos")
            return
        
        
        AccountsDB().store(cbu, type, client_id, alias, balance)

        self.fatherInstance.showTable()
        self.goBack()



class AccountEditWindow(QMainWindow,Ui_CuentasIterableWindow):
    def __init__(self, logedUser, fatherInstance, ID):
        super().__init__()
        self.fatherInstance = fatherInstance
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.updateID = int(ID)
        self.setupUi(self)
        self.handlerCuentas()

    def handlerCuentas(self):
        self.setUser()
        self.uploadValues()
        self.loadValues()
        self.connection()
        
    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[2]}")
    
    def uploadValues(self):
        clients = sql("SELECT * FROM clients;")
        for item in clients:
            listItem = list(item)
            self.slect_titular.addItem(f"{listItem[2]} {listItem[1]}")
            self.slect_titular.setItemData(self.slect_titular.count() - 1, listItem[0])

    def loadValues(self):
        updated = list(sql(f"SELECT * FROM accounts WHERE id = {self.updateID};")[0])
        self.input_balance.hide()
        self.lbl_balance.hide()
        self.input_cbu.setText(f"{updated[1]}")
        self.input_tipo.setText(updated[3])
        self.input_alias.setText(updated[4])
        for index in range(self.slect_titular.count()):
            if self.slect_titular.itemData(index) == updated[2]:
                self.slect_titular.setCurrentIndex(index)
                break


    def connection(self):
        self.btn_back.clicked.connect(self.goBack)
        self.btn_crear.clicked.connect(self.update)

    def goBack(self):
        self.close()
        self.fatherInstance.show()

    def update(self):
        cbu = self.input_cbu.text()
        type = self.input_tipo.text()
        alias = self.input_alias.text()
        client = self.slect_titular.currentIndex()
        client_id = self.slect_titular.itemData(client)
        
        if not cbu:
            QMessageBox.warning(self, "Error", "Rellene el campo CBU")
            return
        if not cbu.isdigit():
            QMessageBox.warning(self, "Error", "El CBU ser numerico")
            return
        validatecbu = sql(f"SELECT * FROM accounts WHERE cbu = '{cbu}';")
        if len(validatecbu) != 0:
            if list(validatecbu[0])[0] != self.updateID:
                QMessageBox.warning(self, "Error", "El cbu ya esta en uso!!")
                return    

        if not type:
            QMessageBox.warning(self, "Error", "Elija un tipo")
            return

        if not alias:
            QMessageBox.warning(self, "Error", "Porfavor Rellene el Alias")
            return
        validatealias = sql(f"SELECT * FROM accounts WHERE alias = '{alias}';")
        if len(validatealias) != 0:
            if list(validatealias[0])[0] != self.updateID:
                QMessageBox.warning(self, "Error", "El  alias ya en uso!!")
                return
        
        
        AccountsDB().update(cbu, type, client_id, alias, self.updateID)

        self.fatherInstance.showTable()
        self.goBack()


        
class HistoryWindow(QMainWindow,Ui_cuentasInfoWindow):
    def __init__(self, logedUser, fatherInstance, ID):
        super().__init__()
        self.fatherInstance = fatherInstance
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.updateID = int(ID)
        self.setupUi(self)
        self.handlerCuentas()

    def handlerCuentas(self):
        self.setUser()
        self.loadTable()
        self.showTable()
        self.connection()
        
    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[2]}")
    
    
    def connection(self):
        self.btn_back.clicked.connect(self.goBack)

    def goBack(self):
        self.close()
        self.fatherInstance.show()

    def loadTable(self):
        self.table_more_info.setColumnCount(5)
        self.table_more_info.setHorizontalHeaderLabels(["ID" , "transaccion", "balance", "tipo", "Creacion"])
        self.table_more_info.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table_more_info.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

    def showTable(self):
        self.table_more_info.setRowCount(0)
        accounts = sql(f"SELECT * FROM histories WHERE account_id = {self.updateID};")
        for item in accounts:
            account = list(item)
            row_position = self.table_more_info.rowCount()
            self.table_more_info.insertRow(row_position)
            self.table_more_info.setItem(row_position, 0, QTableWidgetItem(f"{account[0]}"))
            self.table_more_info.setItem(row_position, 1, QTableWidgetItem(f"{account[1]}"))
            self.table_more_info.setItem(row_position, 2, QTableWidgetItem(f"{account[3]}"))
            self.table_more_info.setItem(row_position, 3, QTableWidgetItem(account[4]))
            self.table_more_info.setItem(row_position, 4, QTableWidgetItem(account[5]))