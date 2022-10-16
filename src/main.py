import sqlite3

#db_cursor.execute("CREATE TABLE books(title, author, genre, asin)")

#db_cursor.execute("""
#        INSERT INTO books VALUES
#            ('Crime And Punishment', 'Fyodor Dostoevsky', 'non-fiction', 00000001),
#           ('The Idiot', 'Fyodor Dostoevsky', 'non-fiction', 00000005)
#            """)

db_connection.commit()

class Database:
    def __init__(self, connection, cursor, name, table_name):
        self.connection = connection
        self.cursor = cursor
        self.name = name
        self.table_name = table_name

    def create(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

    def addTable(self):
        self.cursor.execute("CREATE TABLE {table_name}(title, author, genre, asin)")
    
    def addC
