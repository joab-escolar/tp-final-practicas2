import sqlite3
from utils.print import printGreen
from utils.dateFunctions import getCurrentTime

class AccountsDB:
    def schema(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                cbu INTEGER UNIQUE NOT NULL,
                client_id INTEGER NOT NULL,
                type TEXT,
                alias TEXT UNIQUE NOT NULL CHECK(length(alias) <= 30),
                balance REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (client_id) REFERENCES clients(id)
            );
        ''')
        printGreen("RUN SCHEMA ACCOUNTS")
        db.commit()
        db.close()

    def seed(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute("SELECT * FROM  accounts")
        
        total = cursor.fetchall()

        if len(total) == 0:
            cursor.execute('''
                INSERT INTO accounts (cbu, client_id, type, alias, balance)
                VALUES 
                    (1122334455, 1, 'CUENTA CORRIENTE', 'alias-1', 100000.00),
                    (1234567890, 2, 'CAJA AHORRO', 'alias-2', 40003.33),
                    (6666666666, 1, 'CUENTA CORRIENTE', 'alias-3', 100000.00);
            ''')
            printGreen("RUN SEED ACCOUNTS")

        db.commit()
        db.close()

    # def store(self, username, password, role_id):
    #     db = sqlite3.connect('banco.db')
    #     cursor = db.cursor()

    #     query = '''
    #         INSERT INTO users (username, password, role_id,last_connection)
    #         VALUES (?, ?, ?, ?);
    #     '''

    #     cursor.execute(query, (username, password, role_id, getCurrentTime()))
        
    #     newUser = cursor.fetchall()

    #     db.commit()
    #     db.close()

    #     return newUser


