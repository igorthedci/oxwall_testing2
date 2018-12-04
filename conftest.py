import pytest
from selenium import webdriver
from oxwall_site_model import OxwallSite


@pytest.fixture()
def driver():
    # Open browser driver settings
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    # Close browser
    driver.quit()

@pytest.fixture()
def app(driver):
    app = OxwallSite(driver)
    return app

@pytest.fixture()
def user():
    return {"username": "admin", "password": "pass"}


@pytest.fixture()
def sign_in_session(app, user):
    app.login_as(user)
    yield
    app.logout_as(user)
