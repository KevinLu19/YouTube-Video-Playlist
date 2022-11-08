from mysql.connector import errorcode

import mysql.connector
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import unittest

class TestDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = mysql.connector.connect(host="localhost", user="root", password=f"{os.environ.get('DATABASE_PASSWORD')}", database="music")
        print("Successfully Logged into the database.")
        print("---------------------")

        self.cursor = self.conn.cursor()

        try:
            SQL_COMMAND = "CREATE TABLE IF NOT EXISTS musics (Url VARCHAR(255), Title varchar(255))"
            self.cursor.execute(SQL_COMMAND)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already exists.")
            else:
                print(err.msg)