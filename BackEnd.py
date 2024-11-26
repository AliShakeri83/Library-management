import sqlite3
from tkinter import *

def create_table():
    conn = sqlite3.connect('Library.db')
    curser = conn.cursor()
    curser.execute('create table if not exists tblbook(book_id integer primary key Autoincrement,title text,subject text,author text,publish_year text)')
    conn.commit()
    conn.close()


def insert_data(title , subject, Author, Publish_year):
    conn = sqlite3.connect('Library.db')
    curser = conn.cursor()
    curser.execute("insert into tblBook values(null , ? , ? , ? , ?)" ,(title, subject, Author, Publish_year))
    conn.commit()
    conn.close()


def show_data():
    conn = sqlite3.connect('Library.db')
    curser = conn.cursor()
    curser.execute('select * from tblBook')
    result = curser.fetchall()
    return result


def search(title="" , subject="", Author="", Publish_year=""):
    conn = sqlite3.connect('Library.db')
    curser = conn.cursor()
    curser.execute("select * from tblBook where title=? or subject=? or Author=? or Publish_year=?" ,(title, subject, Author, Publish_year))
    result = curser.fetchall()
    return result

def update_data(book_id,title, subject, Author, Publish_year):
    conn = sqlite3.connect('Library.db')
    curser = conn.cursor()
    curser.execute('update tblBook set title=?, subject=?, Author=?, Publish_year=? where book_id=?' , (title, subject, Author, Publish_year,book_id))
    conn.commit()
    conn.close()
    
    
def delete_data(book_id):
    conn = sqlite3.connect('Library.db')
    curser = conn.cursor()
    curser.execute('delete from tblBook where book_id = ?' , (book_id,))
    conn.commit()
    conn.close()

def New_item(e1 , e2 , e3 , e4):
    conn = sqlite3.connect('Library.db')
    curser = conn.cursor()
    e1.delete(0 , END)
    e2.delete(0 , END)
    e3.delete(0 , END)
    e4.delete(0 , END)
    
    
create_table()
# def main():
#     insert_data('IT' , 'ali', 'c', '1383')
#     show_data()
#     search(title='IT')
#     update_data(10, 'new','new', 'new' , 'new')
#     delete_data(book_id=11)



# if __name__=='__main__':
#     main()