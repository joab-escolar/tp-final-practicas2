"""MAIN"""
import sys
from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox
from PySide6.QtCore import QDateTime 
from view.transacciones import Ui_transanccionWindow
from view.transaccion_create import Ui_transaccionAltaWindow
from utils.sqlRaw import sql
from database.transacctionsDB import TransacctionsDB
from database.historyDB import HistoryDB

class TransacctionWindow(QMainWindow,Ui_transanccionWindow):
    def __init__(self, logedUser, fatherInstance):
        super().__init__()
        self.fatherInstance = fatherInstance
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.setupUi(self)
        self.handlerTransacction()
    
    def handlerTransacction(self):
        self.setUser()
        self.loadTable()
        self.showTable()
        self.connection()

    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[1]}")

    def loadTable(self):
        self.table_transacctions.setColumnCount(6)
        self.table_transacctions.setHorizontalHeaderLabels(["ID" ,"Fecha Impacto", "c. origen", "c. destino", "balance", "Creacion"])
        self.table_transacctions.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table_transacctions.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

    def showTable(self):
        self.table_transacctions.setRowCount(0)
        transacctions = sql("SELECT * FROM transacctions;")
        for item in transacctions:
            transacction = list(item)
            origen =  list(sql(f"SELECT * FROM accounts WHERE id = {transacction[2]}")[0])
            destino =  list(sql(f"SELECT * FROM accounts WHERE id = {transacction[3]}")[0])
            row_position = self.table_transacctions.rowCount()
            self.table_transacctions.insertRow(row_position)
            self.table_transacctions.setItem(row_position, 0, QTableWidgetItem(f"{transacction[0]}"))
            self.table_transacctions.setItem(row_position, 1, QTableWidgetItem(transacction[1]))
            self.table_transacctions.setItem(row_position, 2, QTableWidgetItem(f"{origen[1]}"))
            self.table_transacctions.setItem(row_position, 3, QTableWidgetItem(f"{destino[1]}"))
            self.table_transacctions.setItem(row_position, 4, QTableWidgetItem(f"{transacction[4]}"))
            self.table_transacctions.setItem(row_position, 5, QTableWidgetItem(transacction[5]))


    def connection(self):
        self.btn_back.clicked.connect(self.goBack)
        self.btn_nuevo.clicked.connect(self.showCreate)

    def goBack(self):
        self.close()
        self.fatherInstance.show()

    def showCreate(self):
        self.close()
        self.clientCreate = TransaccitionCreateWindow(self.logedUser, self)
        self.clientCreate.show()

class TransaccitionCreateWindow(QMainWindow,Ui_transaccionAltaWindow):
    def __init__(self, logedUser, fatherInstance):
        super().__init__()
        self.fatherInstance = fatherInstance
        self.logedUser = logedUser
        self.user = list(logedUser[0])
        self.setupUi(self)
        self.handlerTransacction()

    def handlerTransacction(self):
        self.setUser()
        self.uploadValues()
        self.connection()
        
    def setUser(self):
        self.lbl_show_user.setText(f"({self.user[6]}) {self.user[1]}")

    def connection(self):
        self.btn_back.clicked.connect(self.goBack)
        self.btn_create.clicked.connect(self.store)

    def goBack(self):
        self.close()
        self.fatherInstance.show()

    def uploadValues(self):
        clients = sql("SELECT * FROM accounts WHERE status = 1;")
        for item in clients:
            listItem = list(item)
            self.slect_Egreso.addItem(f"{listItem[1]}")
            self.slect_Egreso.setItemData(self.slect_Egreso.count() - 1, listItem[0])
            self.slect_Ingreso.addItem(f"{listItem[1]}")
            self.slect_Ingreso.setItemData(self.slect_Ingreso.count() - 1, listItem[0])

    def store(self):
        balance = self.input_monto.text()
        impact_date = self.input_inpact_date.date().toString("yyyy-MM-dd HH:mm:ss")
        origin = self.slect_Egreso.currentIndex()
        origin_id = self.slect_Egreso.itemData(origin)
        destination = self.slect_Ingreso.currentIndex()
        destination_id = self.slect_Egreso.itemData(destination)


        if origin_id == None:
            QMessageBox.warning(self, "Error", "El origen no puede ser nulo")
            return
        
        if destination_id == None:
            QMessageBox.warning(self, "Error", "El destino no puede ser nulo")
            return
        
        if origin_id == destination_id:
            QMessageBox.warning(self, "Error", "El origen no puede ser el destino")
            return
        
        if not balance:
            QMessageBox.warning(self, "Error", "Por favor rellene el balance")
            return
                
        if not balance.isdigit():
            QMessageBox.warning(self, "Error", "El balance debe ser un numero y no negativo")
            return
        
        
        
        TransacctionsDB().store(impact_date, origin_id, destination_id, float(balance))
        transaccions  = list(sql(f"SELECT * FROM transacctions ORDER BY id DESC LIMIT 1;")[0])
        print(transaccions)

        HistoryDB().store(transaccions[2], transaccions[0], transaccions[4], 'SALIDA')
        HistoryDB().store(transaccions[3], transaccions[0], transaccions[4], 'ENTRADA')

        print(sql("SELECT * FROM histories;"))

        self.fatherInstance.showTable()
        self.goBack()



        