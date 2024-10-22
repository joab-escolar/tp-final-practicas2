import sqlite3
from utils.print import printGreen
from utils.dateFunctions import getCurrentTime

class TransacctionsDB:
    def schema(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transacctions (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                impact_date TIMESTAMP,
                origin_account_id INTEGER NOT NULL,
                destination_account_id INTEGER NOT NULL,
                balance REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (origin_account_id) REFERENCES accounts(id),
                FOREIGN KEY (destination_account_id) REFERENCES accounts(id)
            );
        ''')
        printGreen("RUN SCHEMA TRANSACCTION")
        db.commit()
        db.close()

    def seed(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute("SELECT * FROM  transacctions")
        
        total = cursor.fetchall()

        if len(total) == 0:
            cursor.execute('''
                INSERT INTO transacctions (impact_date, origin_account_id, destination_account_id, balance)
                VALUES ('2024-10-11 00:00:00', 1, 2, 2000.10);
            ''')
            printGreen("RUN SEED TRANSACCTION")

        db.commit()
        db.close()

    def store(self, impact_date, origin_account_id, destination_account_id, balance):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        query = '''
            INSERT INTO transacctions (impact_date, origin_account_id, destination_account_id, balance)
            VALUES (?, ?, ?, ?);
        '''

        cursor.execute(query, (impact_date, origin_account_id, destination_account_id, balance))
        
        created = cursor.fetchall()

        db.commit()
        db.close()

        return created


