from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from page import *


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()


class MainPageTests(BaseTest):
    def test_login_correct(self):
        log_page = LoginPage(self.driver)
        log_page.get_page()
        print(*log_page.elems.btn_sign_in)
        print(lambda driver: driver.find_element(*log_page.elems.btn_sign_in))
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*log_page.elems.btn_sign_in))

if __name__ == "__main__":
    unittest.main()
