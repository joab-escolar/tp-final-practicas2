import sqlite3
from database.UsersDB import UsersDB
from database.RolesDB import RolesDB
from database.clientsDB import ClientsDB
from database.accountsDB import AccountsDB
from database.transacctionsDB import TransacctionsDB
from database.historyDB import HistoryDB

class DataBase:

    def crateDB(self):
        db = sqlite3.connect('banco.db')
        db.commit()
        db.close()

    def migrate(self):
        self.crateDB()

        # Role Region
        role = RolesDB()
        role.schema()
        role.seed()

        # User Region
        users = UsersDB()
        users.schema()
        users.seed()

        # Client Region
        client = ClientsDB()
        client.schema()
        client.seed()

        # Account Region
        account = AccountsDB()
        account.schema()
        account.seed()

        # Transacction Region
        transacction = TransacctionsDB()
        transacction.schema()
        transacction.seed()

        # Transacction Region
        history = HistoryDB()
        history.schema()
        history.seed()
