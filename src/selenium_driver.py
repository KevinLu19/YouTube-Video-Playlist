from msilib.schema import Error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

import time
import playlist

class SeleniumDriver:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        self.extenstion_path = "../uBlock0@raymondhill.net.xpi"
        self.driver.install_addon(self.extenstion_path, temporary=True)

        # self.driver.get("https://www.youtube.com")
        self.current_music_title = ""
        self.current_music_url  = ""
        
        # self.playlist_class = playlist.Playlist()

    def play_song(self):
        # self.driver.get(self.playlist_class)
        self.driver.get("https://www.youtube.com/watch?v=wXhTHyIgQ_U")
        
        # self.current_music_title = self.driver.find_element(By.TAG_NAME, "yt-formatted-string")
        self.current_music_url= self.driver.current_url

        # print (self.current_music_title)

        # .get_attribute("aria-valuenow")
        aria_volume_now = self.driver.find_element(By.CLASS_NAME, "ytp-volume-panel")
        # aria_volume_now.send_keys("5")
        aria_volume_now = self.driver.execute_script("document.querySelector('.ytp-volume-panel div').setAttribute('aria-volume-now','5');")

        # .get_attribute("aria-valuetext")
        # aria_volumetext = self.driver.find_element(By.CLASS_NAME, "ytp-volume-panel").get_attribute("aria-valuetext")
        # aria_volumetext.send_keys("5% volume")
        

        aria_volumetext = self.driver.execute_script("document.querySelector('.ytp-volume-panel div').setAttribute('aria-volumetext','5% volume');")

        print (aria_volume_now)
        # print (aria_volumetext)

    def __exit__(self):
        self.driver.quit()