"""MAIN"""
import sys
from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox
from PySide6.QtCore import QDateTime 
from view.cliente import Ui_clienteWindow
from view.cliente_create import Ui_ClienteIterableWindow
from utils.sqlRaw import sql, sqlCount
from database.clientsDB import ClientsDB

class ClientWindow(QMainWindow,Ui_clienteWindow):
    def __init__(self, logedUser, fatherInstance):
        super().__init__()
        self.fatherInstance = fatherInstance
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.setupUi(self)
        self.handlerClients()
    
    def handlerClients(self):
        self.setUser()
        self.loadTable()
        self.showTable()
        self.connection()

    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[1]}")

    def loadTable(self):
        self.table_clients.setColumnCount(9)
        self.table_clients.setHorizontalHeaderLabels(["ID" ,"nombre", "apellido", "DNI", "fecha nacimiento", "Direccion", "Telefono", "Estado", "Creacion"])
        self.table_clients.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table_clients.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

    def showTable(self):
        self.showStatistics()
        self.table_clients.setRowCount(0)
        clients = sql("SELECT * FROM clients;")
        for item in clients:
            client = list(item)
            row_position = self.table_clients.rowCount()
            self.table_clients.insertRow(row_position)
            self.table_clients.setItem(row_position, 0, QTableWidgetItem(f"{client[0]}"))
            self.table_clients.setItem(row_position, 1, QTableWidgetItem(client[1]))
            self.table_clients.setItem(row_position, 2, QTableWidgetItem(client[2]))
            self.table_clients.setItem(row_position, 3, QTableWidgetItem(f"{client[3]}"))
            self.table_clients.setItem(row_position, 4, QTableWidgetItem(client[4]))
            self.table_clients.setItem(row_position, 5, QTableWidgetItem(client[5]))
            self.table_clients.setItem(row_position, 6, QTableWidgetItem(client[6]))
            self.table_clients.setItem(row_position, 7, QTableWidgetItem(f"{client[7]}"))
            self.table_clients.setItem(row_position, 8, QTableWidgetItem(client[8]))

    def showStatistics(self):
        total_clients = sqlCount("SELECT COUNT(*) FROM clients;")[0]
        total_active_clients = sqlCount("SELECT COUNT(*) FROM clients WHERE status = 1;")[0]
        total_inactive_clients = sqlCount("SELECT COUNT(*) FROM clients WHERE status = 0;")[0]
        top_clientes = ClientsDB().topClients()
        self.lbl_total_clients.setText(f"TOTAL CLIENTES: {total_clients}")
        self.lbl_total_active_clients.setText(f"CLIENTES ACTIVOS: {total_active_clients}")
        self.lbl_total_inactive_clients.setText(f"CLIENTES INNACTIVOS: {total_inactive_clients}")
        self.list_estadistica.clear()
        for item in top_clientes:
            self.list_estadistica.addItem(f"CLIENTE: {item[1]}, TRANS: {item[2]}")

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
        self.clientCreate = ClientCreateWindow(self.logedUser, self)
        self.clientCreate.show()

    def showEdit(self):
        selectedRow = self.table_clients.currentRow()
        if selectedRow >= 0:
            self.close()
            self.clietEdit = UsersEditWindow(self.logedUser, self, self.table_clients.item(selectedRow,0).text())
            self.clietEdit.show()
        else:
            QMessageBox.warning(self, "Error", "Seleccione una fila!!")
            return

    def delete(self):
        selectedRow = self.table_clients.currentRow()
        if selectedRow >= 0:
            deletedID = int(self.table_clients.item(selectedRow,0).text())
            ClientsDB().delete(deletedID)
            self.showTable()
        else:
            QMessageBox.warning(self, "Error", "Seleccione una fila!!")
            return
        
class ClientCreateWindow(QMainWindow,Ui_ClienteIterableWindow):
    def __init__(self, logedUser, fatherInstance):
        super().__init__()
        self.fatherInstance = fatherInstance
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.setupUi(self)
        self.handlerClient()

    def handlerClient(self):
        self.setUser()
        self.connection()
        
    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[1]}")

    def connection(self):
        self.btn_back.clicked.connect(self.goBack)
        self.btn_create.clicked.connect(self.store)

    def goBack(self):
        self.close()
        self.fatherInstance.show()

    def store(self):
        name = self.input_nombre.text()
        lastname = self.input_apellido.text()
        dni = self.input_dni.text()
        birthdate = self.input_fechaN.date().toString("yyyy-MM-dd HH:mm:ss")
        direction = self.input_direccion.text()
        phone = self.input_telefono.text()
        status = 1 if self.btn_activo.isChecked() else 0
        
        if not name:
            QMessageBox.warning(self, "Error", "Rellene el campo nombre")
            return

        if not lastname:
            QMessageBox.warning(self, "Error", "Rellene el campo apellido")
            return
        
        if not dni.isdigit() or len(dni) != 8:
            QMessageBox.warning(self, "Error", "DNI invalido, debe ser numerico y de 8 digitos")
            return
        
        if not birthdate:
            QMessageBox.warning(self, "Error", "Rellene el campo Fecha de nacimiento")
            return
        
        if not direction:
            QMessageBox.warning(self, "Error", "Rellene el campo Direccion")
            return
        
        if not phone:
            QMessageBox.warning(self, "Error", "Rellene el campo Telefono")
            return
        
        if not phone.isdigit():
            QMessageBox.warning(self, "Error", "El numero de telefono debe ser numerico")
            return
        
        if not status:
            QMessageBox.warning(self, "Error", "Seleccione estado")
            return

        newClient = ClientsDB().store(name, lastname, dni, birthdate, direction, phone, status)

        self.fatherInstance.showTable()
        self.goBack()

class UsersEditWindow(QMainWindow,Ui_ClienteIterableWindow):
    def __init__(self, logedUser, fatherInstance, ID):
        super().__init__()
        self.fatherInstance = fatherInstance
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.updateID = int(ID)
        self.setupUi(self)
        self.handlerUsers()

    def handlerUsers(self):
        self.setUser()
        self.loadValues()
        self.connection()
        
    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[1]}")
    
    def loadValues(self):
        updateClient = list(sql(f"SELECT * FROM clients WHERE id = {self.updateID};")[0])
        self.input_nombre.setText(updateClient[1])
        self.input_apellido.setText(updateClient[2])
        self.input_dni.setText(f"{updateClient[3]}")
        self.input_fechaN.setDateTime(QDateTime.fromString(updateClient[4], "yyyy-MM-dd HH:mm:ss"))
        self.input_direccion.setText(updateClient[5])
        self.input_telefono.setText(updateClient[6])
        if updateClient[7] == 1:
            self.btn_activo.setChecked(True)
            self.btn_inactivo.setChecked(False)
        else:
            self.btn_activo.setChecked(False)
            self.btn_inactivo.setChecked(True)


    def connection(self):
        self.btn_back.clicked.connect(self.goBack)
        self.btn_create.clicked.connect(self.update)

    def goBack(self):
        self.close()
        self.fatherInstance.show()

    def update(self):
        name = self.input_nombre.text()
        lastname = self.input_apellido.text()
        dni = self.input_dni.text()
        birthdate = self.input_fechaN.date().toString("yyyy-MM-dd HH:mm:ss")
        direction = self.input_direccion.text()
        phone = self.input_telefono.text()
        status = 1 if self.btn_activo.isChecked() else 0
        
        if not name:
            QMessageBox.warning(self, "Error", "Rellene el campo nombre")
            return

        if not lastname:
            QMessageBox.warning(self, "Error", "Rellene el campo apellido")
            return
        
        if not dni.isdigit() or len(dni) != 8:
            QMessageBox.warning(self, "Error", "DNI invalido, debe ser numerico y de 8 digitos")
            return
        
        if not birthdate:
            QMessageBox.warning(self, "Error", "Rellene el campo Fecha de nacimiento")
            return
        
        if not direction:
            QMessageBox.warning(self, "Error", "Rellene el campo Direccion")
            return
        
        if not phone:
            QMessageBox.warning(self, "Error", "Rellene el campo Telefono")
            return
        
        if not phone.isdigit():
            QMessageBox.warning(self, "Error", "El numero de telefono debe ser numerico")
            return
        
        if not status:
            QMessageBox.warning(self, "Error", "Seleccione estado")
            return
        
        ClientsDB().update(name, lastname, dni, birthdate, direction, phone, status, self.updateID)

        self.fatherInstance.showTable()
        self.goBack()


        