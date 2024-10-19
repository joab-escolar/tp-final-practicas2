import sqlite3
from utils.sqlRaw import sql

class Login():
    def login(self, username, password):
        user = sql(f'''
            SELECT * FROM users WHERE username = '{username}' AND password = '{password}';
        ''')
        if len(user) != 0:
            print(user)
        else:
            print('usuario no encontrado')   
            

