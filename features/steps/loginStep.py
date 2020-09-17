from behave import *


@given("I am on the website")
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login.enter_username(username)
    context.login.enter_pwd(password)


@step("I click login button")
def step_impl(context):
    context.login.click_button()


@then("invalid message should be displayed")
def step_impl(context):
    message = context.login.message_invalid_text()
    assert message, "Invalid credentials"


@then("User must login successfully to the page")
def step_impl(context):
    text = context.homepage.dashboard_message()
    assert text, "Dashboard"
