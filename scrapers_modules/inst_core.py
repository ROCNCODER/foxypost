import time
import json
import os
from loguru import logger
import datetime

from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumwire.utils import decode


logger.add("logs.log", format="{time} {level} {message} {name}", level="ERROR")
class InstagramAggregator():

    def __init__(self, username: str, password: str, link_coll: str):
        self._username = username
        self._password = password
        self._link_coll = link_coll
        self._drive = []
        self._data = []

    def my_response_interceptor(self,request, response):
        if "https://www.instagram.com/api/v1/feed/collection" in request.url and "/posts/" in request.url:
            js = json.loads(decode(response.body, response.headers.get('Content-Encoding', 'identity')))
            data = js["items"]
            for i in data:
                self._data.append({f"https://www.instagram.com/reels/{i['media']['code']}":{"play_count":f"{i['media']['play_count']}","comment_count":f"{i['media']['comment_count']}","like_count":f"{i['media']['like_count']}","date":f"{datetime.datetime.fromtimestamp(i['media']['taken_at']).strftime('%d.%m.%Y')}"}})


    def make_drive(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-setuid-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options = options)
        driver.response_interceptor = self.my_response_interceptor
        return driver

    def authorization(self):
        try:
            self._drive.get("https://www.instagram.com/")
            time.sleep(10)
            login = self._drive.find_element(By.CSS_SELECTOR,
                                             """#loginForm > div > div:nth-child(1) > div > label > input""")
            login.clear()
            login.send_keys(f"{self._username}")
            password = self._drive.find_element(By.CSS_SELECTOR,
                                                """#loginForm > div > div:nth-child(2) > div > label > input""")
            password.clear()
            password.send_keys(f"{self._password}")
            ent = self._drive.find_element(By.CSS_SELECTOR, """#loginForm > div > div:nth-child(3) > button""")
            ent.send_keys(Keys.ENTER)
            time.sleep(10)
        except Exception as f:
            logger.debug(f"Ошибка авторизации {f}")

    def data_search(self):
        self._drive.get(f"{self._link_coll}")
        time.sleep(10)
        SCROLL_PAUSE_TIME = 3
        last_height = self._drive.execute_script("return document.body.scrollHeight")
        while True:
            self._drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = self._drive.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        self._drive.quit()

    def get_data(self):
        try:
            self._drive = self.make_drive()
            self.authorization()
            self.data_search()
        except Exception as f:
            logger.error(f)
        return self._data
