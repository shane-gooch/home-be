from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import os


class GetWebElement:

    def __init__(self):
        self.d = webdriver.Chrome(
            '/Users/shanegooch/Documents/WebDrivers/chromedriver_83')

    def start(self, url, waitTime=10):
        # need to check which version of chrome is being used
        self.d.maximize_window()
        self.d.get(url)
        self.d.implicitly_wait(waitTime)

    def start_headless(self, url, waitTime=10):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        self.d = webdriver.Chrome(
            chrome_options=chrome_options, executable_path="/Users/shanegooch/Documents/WebDrivers/chromedriver_83")
        self.d.get(url)

    def get_element(self, locateBy, locator):
        element = None
        if locateBy == 'id':
            element = self.d.find_element_by_id(locator)
        elif locateBy == 'class':
            element = self.d.find_element_by_class_name(locator)
        elif locateBy == 'css':
            element = self.d.find_element_by_css_selector(locator)
        elif locateBy == 'xpath':
            element = self.d.find_element_by_xpath(locator)
        return element

    def set_wait(self, locator, waitTime=10):
        try:
            element = WebDriverWait(self.d, waitTime).until(
                EC.presence_of_element_located((By.ID, locator)))
        except TimeoutException:
            print("Error: Can't locate element - Quitting Browser")
            self.quit()

    def create_action(self):
        act = ActionChains(self.d)
        return act

    def quit(self):
        self.d.quit()
