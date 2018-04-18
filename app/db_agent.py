# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime

class DataBase:
    conn = sqlite3.connect("twitter.sqlite")
    cursor = conn.cursor()
    def __init__(self):
        self.check_db()

    def check_db(self):
        sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='request';"
        self.cursor.execute(sql)
        if not self.cursor.fetchall():
            print('*** create db ***')
            self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE request (
                                id INTEGER PRIMARY KEY,
                                command varchar(100) NOT NULL, 
                                date varchar(40) NOT NULL)""")

    def record_info(self, command):
        now = datetime.now()
        self.cursor.execute("INSERT INTO request VALUES (NULL , '{command}','{time}')".format(command=command, time=now.strftime("%d-%m-%Y %H:%M")))
        self.conn.commit()

    def get_history(self):
        sql = "SELECT * FROM request;"
        response = self.cursor.execute(sql)
        return (response.fetchall())

    def cleaner(self):
        sql = "DELETE FROM request"
        self.cursor.execute(sql)
        self.conn.commit()