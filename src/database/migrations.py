import sqlite3
from database.UsersDB import UsersDB
from database.RolesDB import RolesDB

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