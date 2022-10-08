from msilib.schema import Error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

import playlist

class SeleniumDriver:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        self.extenstion_path = "../uBlock0@raymondhill.net.xpi"
        self.driver.install_addon(self.extenstion_path, temporary=True)

        # self.driver.get("https://www.youtube.com")
        self.current_music_title = ""
        self.current_music_url  = ""
        
        self.playlist_class = playlist.Playlist()
      
    def play_song(self):
        music_url = self.playlist_class.dequeue_music_url()
        self.driver.get(music_url)
        # print(self.playlist_class.dequeue_music_title())
        # self.driver.get("https://www.youtube.com/watch?v=wXhTHyIgQ_U")

    def __exit__(self):
        self.driver.quit()