from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    menu_hdr_account = (By.ID, "header-account-menu")
    btn_sign_in = (By.ID, "header-account-signin-button1")
