import json
import os.path
import pytest

from data.user_data import user_data
from db.db_connector import DBConnector
from oxwall_site_model import OxwallSite
from value_models.user import User

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json", help="config file")


@pytest.fixture(scope="session")
def config(request):
    filename = request.config.getoption("--config")
    with open(os.path.join(PROJECT_DIR, filename)) as f:
        config = json.load(f)
    admin_data = config["web"]["user"]
    # admin_data.update({"is_admin": True})
    # user_data.append(admin_data)
    return config


@pytest.fixture()
def db(config):
    db = DBConnector(config["db"])
    yield db
    db.close()


@pytest.fixture()
def driver(selenium, base_url):
    # Open browser driver settings
    driver = selenium
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(base_url)
    yield driver
    # Close browser
    driver.quit()


@pytest.fixture()
def app(driver):
    return OxwallSite(driver)

@pytest.fixture()
def admin(config):
    params = config["web"]["user"]
    return User(**params, is_admin=True, real_name=params["username"].title())


@pytest.fixture(params=user_data, ids=[str(user) for user in user_data])
def user(config, request, db):
    user = User(**request.param)
    if not user.is_admin:  # This exception is temporary while admin in user data list
        db.create_user(user)
    yield user
    if not user.is_admin:  # This exception is temporary while admin in user data list
        db.delete_user(user)


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
