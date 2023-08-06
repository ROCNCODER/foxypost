import time
import json
import os

from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumwire.utils import decode

options = webdriver.ChromeOptions()
# options.headless = True
driver = webdriver.Chrome(options=options)


def my_response_interceptor(request, response):
    if "https://www.instagram.com/api/v1/feed/collection" in request.url and "/posts/" in request.url:
        js = json.loads(decode(response.body, response.headers.get('Content-Encoding', 'identity'), ))
        if os.stat("data.json").st_size != 0:
            with open("data.json", 'r') as file:
                data = json.loads(file.read())
                media = js["items"]
                old_data = data["items"]
                old_data = old_data + media
                data["items"] = old_data
            with open("data.json", 'w+') as file:
                json.dump(data, file, indent=4)
        else:
            with open("data.json", 'w') as file:
                json.dump(js, file, indent=4)


driver.response_interceptor = my_response_interceptor


class InstagramAggregator():
    def __init__(self, username: str, password: str, link_coll: str):
        self._username = username
        self._password = password
        self._link_coll = link_coll

    def authorization(self):
        try:
            driver.get("https://www.instagram.com/")
            time.sleep(5)
            login = driver.find_element(By.CSS_SELECTOR,
                                        """#loginForm > div > div:nth-child(1) > div > label > input""")
            login.clear()
            login.send_keys(f"{self._username}")
            password = driver.find_element(By.CSS_SELECTOR,
                                           """#loginForm > div > div:nth-child(2) > div > label > input""")
            password.clear()
            password.send_keys(f"{self._password}")
            ent = driver.find_element(By.CSS_SELECTOR, """#loginForm > div > div:nth-child(3) > button""")
            ent.send_keys(Keys.ENTER)
            time.sleep(10)
        except Exception:
            self.authorization()

    def data_search(self):
        driver.get(f"{self._link_coll}")
        time.sleep(10)
        SCROLL_PAUSE_TIME = 3
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        driver.close()

    @classmethod
    def json_processing(self):
        with open("data.json", "r") as file:
            data = json.loads(file.read())
            data = data["items"]
        data = [{f"https://www.instagram.com/reels/{i['media']['code']}":
                     f"play_count:{i['media']['play_count']} "
                     f"comment_count:{i['media']['comment_count']} "
                     f"like_count:{i['media']['like_count']}"} for i in data]
        f = open('data.json', 'w+')
        f.seek(0)
        f.close()
        return data

    def get_data(self):
        self.authorization()
        self.data_search()
        data = self.json_processing()

        return data

