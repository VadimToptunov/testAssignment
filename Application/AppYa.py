from Pages.YaMainPage import YaMainPageHelper
from selenium import webdriver
import time


class App:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.yandex = YaMainPageHelper(self)

    def yandex_page(self):
        driver = self.driver
        driver.get("https://yandex.ru")

    def quit(self):
        time.sleep(3)
        self.driver.quit()