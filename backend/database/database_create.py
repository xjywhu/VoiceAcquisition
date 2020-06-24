import sqlite3

def createDB(db_name):
    connect = sqlite3.connect(db_name)
    connect.close()