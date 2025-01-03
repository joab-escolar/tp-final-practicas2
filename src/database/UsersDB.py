import sqlite3
from utils.print import printGreen
from utils.dateFunctions import getCurrentTime

class UsersDB:
    def schema(self):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                username TEXT UNIQUE NOT NULL CHECK(length(username) <= 20),
                password TEXT NOT NULL CHECK(length(password) <= 20),
                role_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_connection TIMESTAMP,
                FOREIGN KEY (role_id) REFERENCES roles(id)
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
                INSERT INTO users (username, password, role_id,last_connection)
                VALUES 
                    ('admin', 'admin', 1, '2023-10-10 11:00:00'),
                    ('guest', 'guest', 2, '2023-10-10 11:00:00');
            ''')
            printGreen("RUN SEED USERS")

        db.commit()
        db.close()

    def store(self, username, password, role_id):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        query = '''
            INSERT INTO users (username, password, role_id,last_connection)
            VALUES (?, ?, ?, ?);
        '''

        cursor.execute(query, (username, password, role_id, getCurrentTime()))
        
        newUser = cursor.fetchall()

        db.commit()
        db.close()

        return newUser
    
    def update(self, username, password, role_id, id):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        if len(password) > 0:
            cursor.execute(f"UPDATE users SET username = '{username}', password = '{password}', role_id = {role_id} WHERE id = {id};")
        else:
            cursor.execute(f"UPDATE users SET username = '{username}', role_id = {role_id} WHERE id = {id};")
        
        updatedUser = cursor.fetchall()

        db.commit()
        db.close()

        return updatedUser

    def delete(self, id):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()

        cursor.execute(f"DELETE FROM users WHERE id = {id};")

        deletedUser = cursor.fetchall()

        db.commit()
        db.close()

        return deletedUser


