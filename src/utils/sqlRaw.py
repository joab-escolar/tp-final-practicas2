import sqlite3

def sql(query):
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()

    cursor.execute(query)
    response =  cursor.fetchall()

    db.commit()
    db.close()
    
    return response

def sqlCount(query):
    db = sqlite3.connect('banco.db')
    cursor = db.cursor()

    cursor.execute(query)
    response =  cursor.fetchall()

    db.commit()
    db.close()
    
    return list(response[0])