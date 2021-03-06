import sqlite3
import pymysql


class DBHelper:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='todoVIO')

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS items (description text, owner text)"
        self.conn.cursor().execute(tblstmt)
        self.conn.commit()

    def add_item(self, item_text, owner):
        stmt = "INSERT INTO items (description,owner) VALUES (%s,%s)"
        args = (item_text, owner)
        self.conn.cursor().execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text,owner):
        stmt = "DELETE FROM items WHERE description = (%s) AND owner = (%s)"
        args = (item_text, owner)
        self.conn.cursor().execute(stmt, args)
        self.conn.commit()

    def get_items(self,owner):
        stmt = """SELECT description FROM items WHERE owner=(%s)"""
        args = (owner,)
        cursor= self.conn.cursor()
        exc= cursor.execute(stmt,args)
        data= cursor.fetchall()
        return [x[0] for x in data]
