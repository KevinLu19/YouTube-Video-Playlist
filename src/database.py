# import sqlite3

# class Database:
#     def __init__(self):
#         self.conn = sqlite3.connect("database.db")
#         self.cursor = self.conn.cursor()
#         self.cursor.execute("CREATE TABLE IF NOT EXISTS music(music_urls, titles);")
        
#         try:
#             self.cursor.execute("create unique index qnu_music_2 on music(music_urls, titles);")
#         except sqlite3.OperationalError as e:
#             print (e)

#     def add_entry(self, music_url, music_title):
#         self.add = self.cursor.execute(f"INSERT OR IGNORE INTO music (music_urls, titles) VALUES(?, ?)", (music_url, music_title))
#         self.conn.commit()

#     def fetch_entry(self):
#         self.cursor.fetchall()

import mysql.connector
from credentials import PASSWORD

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="Music")
    
    def __exit__(self):
        self.conn.close()