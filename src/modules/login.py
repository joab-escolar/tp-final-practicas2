import sqlite3
from utils.sqlRaw import sql

class Login():
    def login(self, username, password):
        user = sql(f'''
            SELECT * FROM users WHERE username = '{username}' AND password = '{password}';
        ''')
        if len(user) != 0:
            return sql(f"SELECT users.*, roles.name FROM users JOIN roles ON users.role_id = roles.id WHERE users.id = {list(user[0])[0]};")
        else:
            return False  
            

