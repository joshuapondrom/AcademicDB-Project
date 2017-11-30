import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE Student('
               '    id INTEGER PRIMARY KEY,'
               '    address VARCHAR(100),'
               '    Name VARCHAR(50),'
               '    Year INTEGER'
               ')' )
connection.commit()
cursor.close()