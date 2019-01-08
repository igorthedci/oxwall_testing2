import pytest
from selenium import webdriver

from oxwall_site_model import OxwallSite
from value_models.user import User


@pytest.fixture()
def driver():
    # Open browser driver settings
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    # driver.get('http://127.0.0.1/oxwall/')
    yield driver
    # Close browser
    driver.quit()


@pytest.fixture()
def user():
    return User(username="admin", password="pass", real_name="Admin")


@pytest.fixture()
def signed_in_user(driver, user):
    app = OxwallSite(driver)
    app.login_as(user)
    yield user
    app.logout_as(user)
