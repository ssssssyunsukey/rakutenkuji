import time
from selenium import webdriver
# 最新のchromeのversionへ合わせるため。
from webdriver_manager.chrome import ChromeDriverManager

class Selenium:
    driver  = None
    element = None

    def __init__(self):
        options = webdriver.ChromeOptions()
        # ブラウザを開くことなくバックグラウンドにて実行する。
        # options.add_argument('--headless')

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # ブラウジングするwindow幅を設定する。
        self.driver.set_window_size(1300, 1040)

    def access(self, url):
        self.driver.get(url)

    def find_element_by_id(self, name):
        self.element = self.driver.find_element_by_id(name)

    def find_element_css_name(self, name):
        self.element = self.driver.find_element_by_css_selector(name)

    def find_element_xpath(self, name):
        self.element = self.driver.find_element_by_xpath(name)

    def set_value(self, value):
        self.element.send_keys(value)

    def click(self):
        self.element.click()

    def stop(self, num):
        time.sleep(num)

    def quit(self):
        self.driver.quit()
