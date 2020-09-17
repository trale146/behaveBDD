from Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.dashboard = Locators.dashboard_xpath

    def dashboard_message(self):
        dashboard_text = self.driver.find_element_by_xpath(self.dashboard).text
        return dashboard_text
