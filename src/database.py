from mysql.connector import errorcode

import mysql.connector
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import youtube

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password=f"{os.environ.get('DATABASE_PASSWORD')}", database="music")
        print("Logged into the database.")
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

    def get_title_and_url_from_youtube(self):
        youtube_obj = youtube.YouTubeSearch()
        music_title = youtube_obj.get_music_title()
        music_url = youtube_obj.get_music_url()

        return (music_title, music_url)

    def __add_entry(self, music_url, music_title):
        video_meta_data = self.get_title_and_url_from_youtube()
        music_url = video_meta_data[1]
        music_title = video_meta_data[0]

        SQL_COMMAND = f"INSERT IGNORE INTO musics(Url, Title) VALUES('{music_url}', '{music_title}');"

        try:
            self.cursor.execute(SQL_COMMAND)
            print("Added value into the table.")

            self.conn.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            self.conn.rollback()
        
    def add_unique_identifier_to_column(self):
        SQL_COMMAND = "ALTER TABLE musics ADD UNIQUE INDEX(url)"
        self.cursor.execute(SQL_COMMAND)

    def fetch_music_url(self):
        SQL_COMMAND = "SELECT Url FROM musics;"

        self.cursor.execute(SQL_COMMAND)
        
        return self.cursor.fetchall()

    def fetch_music_title(self):
        SQL_COMMAND  = "SELECT Title FROM musics;"

        self.cursor.execute(SQL_COMMAND)

        return self.cursor.fetchall()

    def __drop_table(self):
        try:
            self.cursor.execute("DROP TABLE musics")
            print("Successfully dropped table Musics.")
        except mysql.connector.Error as err:
            print(err.msg)

    def __exit__(self):
        if self.conn is not None and self.conn.is_connected():
            self.conn.close()