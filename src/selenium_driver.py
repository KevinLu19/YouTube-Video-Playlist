from msilib.schema import Error
from tkinter import E
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

class SeleniumDriver:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        
        try:
            self.driver.get("https://www.youtube.com")
            time.sleep(5)
            self.driver.quit()

        except Error as E:
            print(E)
