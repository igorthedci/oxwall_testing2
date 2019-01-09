import json
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


with open("user_data.json", encoding="utf8") as f:
    user_data = json.load(f)


@pytest.fixture(params=user_data, ids=[str(user) for user in user_data])
def user(request):
    return User(**request.param)


@pytest.fixture()
def signed_in_user(driver, user):
    app = OxwallSite(driver)
    app.login_as(user)
    yield user
    app.logout_as(user)


@pytest.fixture()
def logout(driver):
    yield
    app = OxwallSite(driver)
    app.dash_page.sign_out()
