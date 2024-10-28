import sqlite3
from utils.sqlRaw import sql
from utils.dateFunctions import getCurrentTime

class Login():
    def login(self, username, password):
        user = sql(f'''
            SELECT * FROM users WHERE username = '{username}' AND password = '{password}';
        ''')
        if len(user) != 0:
            self.setLastLogin(list(user[0])[0])
            return sql(f"SELECT users.*, roles.name FROM users JOIN roles ON users.role_id = roles.id WHERE users.id = {list(user[0])[0]};")
        else:
            return False  
    
    def setLastLogin(self, id):
        sql(f'''
            UPDATE users SET last_connection = '{getCurrentTime()}' WHERE id = {id};
            ''')

