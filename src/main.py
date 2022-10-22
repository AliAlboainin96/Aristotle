import sqlite3

#db_cursor.execute("CREATE TABLE books(title, author, genre, asin)")

#db_cursor.execute("""
#        INSERT INTO books VALUES
#            ('Crime And Punishment', 'Fyodor Dostoevsky', 'non-fiction', 00000001),
#           ('The Idiot', 'Fyodor Dostoevsky', 'non-fiction', 00000005)
#            """)

# db_connection.commit()

class Book:
    
    def __init__(self, author, title, genre, asin, book_id, num_pages):
        self.author = author
        self.title = title
        self.genre = genre
        self.asin = asin
        self.book_id = book_id
        self.num_pages = num_pages
    

class Database:
    
    def __init__(self, db_name):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.db_name = db_name

    
    def addTable(self):
        self.cursor.execute("CREATE TABLE Books(title, author, genre, asin)")
        
    
    def addBook(self):
        self.cursor.execute()


    def __del__(self):
        self.connection.close()



if __name__ == '__main__':
    db1 = Database("lib.db")
    db1.addTable()
    db1.addBook()
