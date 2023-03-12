import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Browser:
    browser, service = None, None

    def __init__(self, driver):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)
        
    def open_page(self, url):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()


if __name__ == '__main__':
    browser = Browser('drivers/chromedriver.exe')
    browser.open_page('https://www.google.com')
    time.sleep(3)
    browser.open_page('https://www.browserstack.com/selenium')
    time.sleep(3)
    browser.close_browser()