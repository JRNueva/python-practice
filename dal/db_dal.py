import sqlite3
from abc import ABC

class DbDaoABC:
    
    def __get_db_connection(self):
            return sqlite3.connect('address_book.db')
        
    def execute_select(self, sql):
        conn = self.__get_db_connection()
        return conn.execute(sql)