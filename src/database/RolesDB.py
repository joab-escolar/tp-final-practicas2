import sqlite3
from utils.print import printGreen

class RolesDB:
    def schema(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS roles (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE NOT NULL CHECK(length(name) <= 20)
            );
        ''')
        printGreen("RUN SCHEMA ROLE")
        db.commit()
        db.close()

    def seed(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute("SELECT * FROM  roles")
        
        total = cursor.fetchall()

        if len(total) == 0:
            cursor.execute('''
                INSERT INTO roles (name)
                VALUES 
                    ('ADMINISTRADOR'),
                    ('INVITADO');
            ''')
            printGreen("RUN SEED ROLE")

        db.commit()
        db.close()


