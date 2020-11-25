import sqlite3

connection = sqlite3.connect('C:\\Users\\HP\\Desktop\\quarantine_time\\sqlite-tools-win32-x86-3310100\\data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
#create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
#cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS students (name text PRIMARY KEY, city text)"
cursor.execute(create_table)

connection.commit()

connection.close()
