from locators import *


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    url_base = "https://www.expedia.com/"
    url_path = ""
    url = ""
    title = ""


    def __init__(self, driver):
        self.driver = driver
        self.url = self.url_base + self.url_path

    def set_val_to(self, val, locator):
        self.driver.find_elem(*locator).send_keys()

    def get_page(self):
        self.driver.get(self.url)
        assert self.title in self.driver.title



class LoginPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    title = "Expedia Travel: Vacations, Cheap Flights, Airline Tickets & Airfares"

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.elems = LoginPageLocators()



    def log_in(self):
        pass

class NewPage(BasePage):
    url_path = "url_path"