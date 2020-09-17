from selenium.webdriver.common.by import By

from Locators.locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        # retrieve value from locators
        self.username_txt_id = Locators.username_txt_id
        self.pwd_txt_id = Locators.pwd_txt_id
        self.login_button_id = Locators.login_button_id
        self.message_invalid_id = Locators.message_invalid_id

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_txt_id).clear()
        self.driver.find_element_by_id(self.username_txt_id).send_keys(username)

    def enter_pwd(self, pwd):
        self.driver.find_element_by_id(self.pwd_txt_id).clear()
        self.driver.find_element_by_id(self.pwd_txt_id).send_keys(pwd)

    def click_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def message_invalid_text(self):
        message = self.driver.find_element_by_id(self.message_invalid_id).text
        return message

