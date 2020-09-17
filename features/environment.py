from selenium import webdriver
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage


def before_scenario(context, scenario):
    print("Before scenario\n")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.login = LoginPage(context.driver)
    context.homepage = HomePage(context.driver)


def after_scenario(context, scenario):
    print("scenario status:" + str(scenario.status))
    context.driver.close()
