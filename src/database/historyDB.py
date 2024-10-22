import sqlite3
from utils.print import printGreen
from utils.dateFunctions import getCurrentTime

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


