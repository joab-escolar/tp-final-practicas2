import sqlite3
from utils.print import printGreen
from utils.dateFunctions import getCurrentTime

class ClientsDB:
    def schema(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT NOT NULL CHECK(length(name) <= 20),
                lastname TEXT NOT NULL CHECK(length(lastname) <= 20),
                dni INTEGER NOT NULL,
                birthdate TIMESTAMP NOT NULL,
                direction TEXT NOT NULL CHECK(length(direction) <= 100),
                phone TEXT NOT NULL CHECK(length(phone) <= 20),
                status INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        printGreen("RUN SCHEMA CLIENTS")
        db.commit()
        db.close()

    def seed(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute("SELECT * FROM  clients")
        
        total = cursor.fetchall()

        if len(total) == 0:
            cursor.execute('''
                INSERT INTO clients (name, lastname, dni, birthdate, direction, phone, status)
                VALUES 
                    ('cliente1', 'apellido1', 44226597, '2002-06-11 00:00:00', 'Callex Posadas', '3764-xxxxxx', 1),
                    ('cliente2', 'apellido2', 12345678, '2009-10-11 00:00:00', 'Av Posadas', '3764-oooooo', 0);
            ''')
            printGreen("RUN SEED CLIENTS")

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


