from msilib.schema import Error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import playlist

class SeleniumDriver:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        self.extenstion_path = "../uBlock0@raymondhill.net.xpi"
        self.driver.install_addon(self.extenstion_path, temporary=True)
        self.driver.get("https://www.youtube.com")
        self.current_music_title = ""
        self.current_music_url  = ""

    def __exit__(self):
        self.driver.quit()