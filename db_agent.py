# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime


class DataBase:
    conn = sqlite3.connect("twitter.sqlite")
    cursor = conn.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE request (
                                id INTEGER PRIMARY KEY,
                                command varchar(100) NOT NULL, 
                                date varchar(40) NOT NULL)""")
        self.conn.close()

    def record_info(self, command):
        now = datetime.now()
        self.cursor.execute("INSERT INTO request VALUES (NULL , '{command}','{time}')".format(command=command, time=now.strftime("%d-%m-%Y %H:%M")))
        self.conn.commit()
        self.conn.close()

    def cleaner(self):
        sql = "DELETE FROM request"
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()