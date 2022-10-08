from selenium_driver import SeleniumDriver

import playlist
import database
import youtube
import os 

def main():
    selenium_driver = SeleniumDriver()
    # music_database = database.Database()
    # music_playlist = playlist.Playlist()

    # music_playlist.add_entry("https://www.youtube.com/watch?v=6s4_EWHzv_o&list=FLhPx5RAYjdns77CKe7Vn2tA&index=19", Need title name here.)
    
    # music_database.add_entry("https://www.youtube.com/watch?v=6s4_EWHzv_o&list=FLhPx5RAYjdns77CKe7Vn2tA&index=19", "one direction - night changes")
    # print(music_database.fetch_entry())

    selenium_driver.play_song()
    
    # print (os.environ.get('DATABASE_PASSWORD'))
    # print (f"Password is: {os.environ.get('DATABASE_PASSWORD')}")

    

if __name__ == "__main__":
    main()