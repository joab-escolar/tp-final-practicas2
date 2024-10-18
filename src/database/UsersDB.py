import sqlite3
from utils.print import printGreen

class UsersDB:
    def schema(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                username TEXT UNIQUE NOT NULL CHECK(length(username) <= 20),
                password TEXT NOT NULL CHECK(length(password) <= 20),
                role INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_connection TIMESTAMP,
                FOREIGN KEY (role) REFERENCES roles(id)
            );
        ''')
        printGreen("RUN SCHEMA USER")
        db.commit()
        db.close()

    def seed(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute("SELECT * FROM  users")
        
        totalUsers = cursor.fetchall()

        if len(totalUsers) == 0:
            cursor.execute('''
                INSERT INTO users (username, password, role,last_connection)
                VALUES 
                    ('admin', 'admin', 1, '2023-10-10 11:00:00'),
                    ('guest', 'guest', 2, '2023-10-10 11:00:00');
            ''')
            printGreen("RUN SEED USERS")

        db.commit()
        db.close()


