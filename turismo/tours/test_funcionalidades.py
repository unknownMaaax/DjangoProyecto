from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TourViewsFunctionalTestCase(LiveServerTestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()


