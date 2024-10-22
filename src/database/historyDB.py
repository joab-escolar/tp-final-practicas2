import sqlite3
from utils.print import printGreen
from utils.dateFunctions import getCurrentTime
from utils.sqlRaw import sql

class HistoryDB:
    def schema(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS histories (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                account_id INTEGER,
                transacction_id INTEGER,
                balance REAL NOT NULL,
                type TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_id) REFERENCES accounts(id),
                FOREIGN KEY (transacction_id) REFERENCES transacctions(id)
            );
        ''')
        printGreen("RUN SCHEMA HISTORY")
        db.commit()
        db.close()

    def seed(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute("SELECT * FROM  histories")
        
        total = cursor.fetchall()

        if len(total) == 0:
            cursor.execute('''
                INSERT INTO histories (account_id, transacction_id, balance, type)
                VALUES 
                        (1, 1, 2000.10, 'ENTRADA'),
                        (2, 1, 2000.10, 'SALIDA');
            ''')
            printGreen("RUN SEED HISTORY")

        db.commit()
        db.close()

    def store(self, account_id, transacction_id, balance, type):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        query = '''
            INSERT INTO histories (account_id, transacction_id, balance, type)
            VALUES (?, ?, ?, ?);
        '''

        cursor.execute(query, (account_id, transacction_id, balance, type))
        
        created = cursor.fetchall()

        account = list(sql(f"SELECT * FROM accounts WHERE id = {account_id};")[0])
        newBalance = 0 
        if type == "ENTRADA":
            newBalance = float(account[5]) + float(balance)
        else:
            newBalance = float(account[5]) - float(balance)

        cursor.execute(f"UPDATE accounts SET balance = {newBalance} WHERE id = {account_id}")


        db.commit()
        db.close()

        return created


