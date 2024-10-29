import sqlite3
from utils.print import printGreen
from utils.dateFunctions import getCurrentTime
from utils.sqlRaw import sql

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
                status status INTEGER DEFAULT 1,
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

    def store(self, cbu, type, client_id, alias, balance):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        query = '''
            INSERT INTO accounts (cbu, client_id, type, alias, balance)
            VALUES (?, ?, ?, ?, ?);
        '''

        cursor.execute(query, (cbu, client_id, type, alias, balance))
        
        newAccount = cursor.fetchall()

        db.commit()
        db.close()

        return newAccount

    def update(self, cbu, type, client_id, alias, id):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        query = f"UPDATE accounts SET cbu = {cbu}, client_id = {client_id}, type = '{type}' , alias = '{alias}' WHERE id = {id};"

        cursor.execute(query)
        
        updated = cursor.fetchall()

        db.commit()
        db.close()

        return updated
    
    def delete(self, id):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()


        cursor.execute(f"UPDATE accounts SET status = 0 WHERE id = {id}")
        
        updated = cursor.fetchall()

        db.commit()
        db.close()

        return updated
    
    def getTopAccounts(self):
        accounts = sql("SELECT * FROM accounts WHERE status = 1;")
        top_accounts = []
        for element in accounts:
            account = list(element)[0]
            transacctions = list(sql(f'''
                SELECT accounts.id, accounts.alias, COUNT(histories.id) AS total_histories
                FROM accounts
                LEFT JOIN histories ON histories.account_id = accounts.id
                WHERE accounts.id = {account}
                GROUP BY accounts.id, accounts.alias;
            ''')[0])
            top_accounts.append(transacctions)
        top_accounts = sorted(top_accounts, key=lambda x: x[2], reverse=True)
        top_accounts = top_accounts[:10]
        return top_accounts


