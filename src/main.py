from selenium_driver import SeleniumDriver

import playlist
import database
import youtube
import os 

def input_song_name():
    user_input = input("Enter in song name: ")

    return user_input

def main():
    music_database = database.Database()
    song_name =  input_song_name()
    music_database.user_input_handler(song_name)
    # music_playlist = playlist.Playlist()

    # music_playlist.add_entry("https://www.youtube.com/watch?v=6s4_EWHzv_o&list=FLhPx5RAYjdns77CKe7Vn2tA&index=19", Need title name here.)
    # music_database.add_entry("https://www.youtube.com/watch?v=ul7u6ZfAaYw", "post malone - circles (slowed + reverb)")

    selenium_driver = SeleniumDriver()
    selenium_driver.play_song()
    
    # print (os.environ.get('DATABASE_PASSWORD'))
    # print (f"Password is: {os.environ.get('DATABASE_PASSWORD')}")

if __name__ == "__main__":
    main()